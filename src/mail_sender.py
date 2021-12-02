import os
import smtplib
import time
from email.message import EmailMessage

from . import utils


def clear_logs():
    """Clears log files of emails sent and not sent"""
    try:
        os.remove("logs/sent.log")
        os.remove("logs/notsent.log")
    except FileNotFoundError:
        return
    except Exception as e:
        raise e


def message_replace(user: str, uuid: str, confirm_link: str, message: str) -> str:
    """Replace tags in message with given information."""
    message = message.replace("{user}", user)
    message = message.replace("{confirm_link}", (confirm_link + uuid))
    return message


def send_mails(config: dict, receivers: map):
    """Sends mails to given receivers, with a given link."""
    sender_mail = config["mail"]
    sender_password = config["password"]
    with open(f"config/{config['mail_template']}", encoding="utf-8", mode="rt") as file:
        message_content = file.read()
    with smtplib.SMTP(config["host"], config["port"]) as smtp_client:
        # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        smtp_client.starttls()
        smtp_client.login(sender_mail, sender_password)
        clear_logs()
        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = config["subject"]
            content = message_replace(
                receiver.name, receiver.uuid, config["confirm_link"], message_content)
            message.set_content(content)
            time.sleep(10)
            try:
                smtp_client.sendmail(
                    sender_mail, receiver.mail, message.as_string())
                print(f"{receiver.mail} sent")
                utils.log(f"{utils.current_time()} {receiver.mail} sent")
                utils.log_to_file("sent.log", f"{receiver.mail}")
            except Exception as e:
                print(f"{receiver.mail} not sent, exception: {e}")
                utils.log(
                    f"{utils.current_time()} {receiver.mail} not sent, reason: {e}")
                utils.log_to_file("notsent.log", f"{receiver.mail}")
