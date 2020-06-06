import smtplib
import json
from email.message import EmailMessage

mail_user = "informatyzacja@student.pwr.edu.pl"
mail_password = ""
sending_mail = smtplib.SMTP('student.pwr.edu.pl', 587)


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
def send_mails(receivers, subject: str, msg_content: str):
    for receiver in receivers:
        message = EmailMessage()
        message['Subject'] = subject
        message.set_content(msg_content)
        sending_mail.sendmail(mail_user, receiver.mail, message.as_string())


if __name__ == "__main__":
    user_data = read_json("results.json")  # plik json z mailami
    mail_receivers = map(lambda x: MailReceiver(x), user_data)
    send_mails(mail_receivers, "TEMAT", "WIADOMOSC")
