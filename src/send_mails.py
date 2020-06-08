import smtplib
import json
from email.message import EmailMessage


class MailReceiver:
    def __init__(self, receiver_properties: dict):
        self.name = receiver_properties["Name"]
        self.mail = receiver_properties["Mail"]
        self.uuid = receiver_properties["UUID"]


def read_json(filename: str):
    with open(filename) as file:
        data = json.load(file)
    return data


def generate_message_content(user, uuid, link, message):
    message = message.replace("{user}", user)
    message = message.replace("{link}", (link + uuid))
    return message


def send_mails(mail_data_dict, receivers, link):
    mail_user = mail_data_dict["Mail"]
    mail_password = mail_data_dict["Password"]
    with open(mail_data_dict["MessageContentFile"], encoding="utf-8", mode="rt") as file:
        message_content = file.read()
    with smtplib.SMTP(mail_data_dict["Host"], mail_data_dict["Port"]) as sending_mail:
        sending_mail.starttls()  # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        sending_mail.login(mail_user, mail_password)
        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = mail_data_dict["Subject"]
            content = generate_message_content(receiver.name, receiver.uuid, link, message_content)
            message.set_content(content)
            sending_mail.sendmail(mail_user, receiver.mail, message.as_string())


if __name__ == "__main__":
    mail_dict = read_json("../mail_data.json")[0]  # [0] to get the dict
    user_data = read_json(mail_dict["JSONFile"])  # mail receivers json file
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(mail_dict, mail_receivers, "https://www.unclelukes.site:33862/Confirm?uuid=")
