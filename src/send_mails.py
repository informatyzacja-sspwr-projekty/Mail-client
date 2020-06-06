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


# todo potem zmienić msg_content na listę stringów?
#  bo dla każdego odbiorcy chyba trzeba osobną treść
def send_mails(mail_data, receivers, subject: str, msg_content: str):
    mail_user = mail_data["Mail"]
    mail_password = mail_data["Password"]
    with smtplib.SMTP(mail_data["Host"], mail_data["Port"]) as sending_mail:
        sending_mail.starttls()  # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls
        sending_mail.login(mail_user, mail_password)
        for receiver in receivers:
            message = EmailMessage()
            message['Subject'] = subject
            message.set_content(msg_content)
            sending_mail.sendmail(mail_user, receiver.mail, message.as_string())


if __name__ == "__main__":
    mail_dataa = read_json("../mail_login.json")[0]  # [0] to get the dict
    user_data = read_json("../results.json")  # mail receivers json file
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(mail_dataa, mail_receivers, "TEMAT", "WIADOMOSC")
