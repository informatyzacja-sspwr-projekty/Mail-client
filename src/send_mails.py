#!/usr/bin/env python
# -*- coding: latin-1 -*-
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


def message_content(mail_data, uuid, user, message):
    message = message.replace("<user>", user)
    message = message.replace("<link>", ("<Link z API>" + uuid))
    return message


# todo potem zmienić msg_content na listę stringów?
#  bo dla każdego odbiorcy chyba trzeba osobną treść
def send_mails(mail_data, receivers):
    mail_user = mail_data["Mail"]
    mail_password = mail_data["Password"]
    filename = mail_data["Message_content"]
    with open(filename, encoding="utf-8", mode="rt") as file:
        my_message = file.read()

    with smtplib.SMTP(mail_data["Host"], mail_data["Port"]) as sending_mail:
        sending_mail.starttls()  # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        sending_mail.login(mail_user, mail_password)

        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = mail_data["Subject"]
            msg_content = message_content(mail_data, receiver.uuid, receiver.name, my_message)
            message.set_content(msg_content)
            sending_mail.sendmail(mail_user, receiver.mail, message.as_string())


if __name__ == "__main__":
    mail_dataa = read_json("../mail_login.json")[0]  # [0] to get the dict
    user_data = read_json("Conversion_results.json")  # mail receivers json file
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(mail_dataa, mail_receivers)
