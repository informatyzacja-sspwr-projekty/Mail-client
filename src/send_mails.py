import os
import smtplib
import time
from email.message import EmailMessage

from . import utils


class MailReceiver:
    """Class made to simplify handling mail receivers."""

    def __init__(self, receiver_properties: dict):
        self.name = receiver_properties["name"]
        self.mail = receiver_properties["mail"]
        self.uuid = receiver_properties["uuid"]


def message_replace(user, uuid, link, message):
    """Replace tags in message with given information."""
    message = message.replace("{user}", user)
    message = message.replace("{link}", (link + uuid))
    return message


def send_mails(mail_data_dict, receivers, link):
    """Sends mails to given receivers, with a given link."""
    mail_user = mail_data_dict["mail"]
    mail_password = mail_data_dict["password"]
    with open(mail_data_dict["mail_template"], encoding="utf-8", mode="rt") as file:
        message_content = file.read()
    with smtplib.SMTP(mail_data_dict["host"], mail_data_dict["port"]) as sending_mail:
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        sending_mail.starttls()
        sending_mail.login(mail_user, mail_password)
        os.remove("logs/sent.log")
        os.remove("logs/notsent.log")
        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = mail_data_dict["subject"]
            content = message_replace(
                receiver.name, receiver.uuid, link, message_content)
            message.set_content(content)
            time.sleep(10)
            try:
                sending_mail.sendmail(
                    mail_user, receiver.mail, message.as_string())
                print(f"{receiver.mail} sent")
                utils.log(f"{utils.current_time()} {receiver.mail} sent")
                utils.log_to_file("sent.log", f"{receiver.mail}")
            except Exception as e:
                print(f"{receiver.mail} not sent, exception: {e}")
                utils.log(
                    f"{utils.current_time()} {receiver.mail} not sent, reason: {e}")
                utils.log_to_file("notsent.log", f"{receiver.mail}")


if __name__ == "__main__":
    config = utils.load_config(
        "../mail_data.json")
    # mail receivers json file
    user_data = utils.read_json(config["mails_json_file"])
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(config, mail_receivers,
               "https://www.unclelukes.site:33862/Confirm?uuid=")
    print("Mails have been sent!")
