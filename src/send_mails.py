import datetime
import json
import smtplib
import time
from email.message import EmailMessage


def current_time() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


class MailReceiver:
    """Class made to simplify handling mail receivers."""

    def __init__(self, receiver_properties: dict):
        self.name = receiver_properties["Name"]
        self.mail = receiver_properties["Mail"]
        self.uuid = receiver_properties["UUID"]


def read_json(filename: str):
    """Reads a JSON file and returns it as a list of dictionaries."""
    with open(filename) as file:
        data = json.load(file)
    return data


def message_replace(user, uuid, link, message):
    """Replace tags in message with given information."""
    message = message.replace("{user}", user)
    message = message.replace("{link}", (link + uuid))
    return message


def send_mails(mail_data_dict, receivers, link):
    """Sends mails to given receivers, with a given link."""
    mail_user = mail_data_dict["Mail"]
    mail_password = mail_data_dict["Password"]
    with open(mail_data_dict["MessageContentFile"], encoding="utf-8", mode="rt") as file:
        message_content = file.read()
    with smtplib.SMTP(mail_data_dict["Host"], mail_data_dict["Port"]) as sending_mail:
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        sending_mail.starttls()
        sending_mail.login(mail_user, mail_password)
        log_file = open("../log.txt", 'a')
        sent_file = open("../sent.txt", 'w')
        notsent_file = open("../notsent.txt", 'w')
        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = mail_data_dict["Subject"]
            content = message_replace(
                receiver.name, receiver.uuid, link, message_content)
            message.set_content(content)
            time.sleep(10)
            try:
                sending_mail.sendmail(
                    mail_user, receiver.mail, message.as_string())
                print(f"{receiver.mail} sent")
                log_file.write(f"{current_time()} {receiver.mail} sent")
                sent_file.write(f"{receiver.mail}")
            except Exception as e:
                print(f"{receiver.mail} not sent, exception: {e}")
                log_file.write(
                    f"{current_time()} {receiver.mail} not sent, reason: {e}")
                notsent_file.write(f"{receiver.mail}")
        log_file.close()
        sent_file.close()
        notsent_file.close()


if __name__ == "__main__":
    mail_dict = read_json("../mail_data.json")[0]  # [0] to get the dict
    # mail receivers json file
    user_data = read_json(mail_dict["MailsJsonFile"])
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(mail_dict, mail_receivers,
               "https://www.unclelukes.site:33862/Confirm?uuid=")
    print("Mails have been sent!")
