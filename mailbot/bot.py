#-*- coding: utf-8 -*-
import re
import smtplib
import mailbot.tuple as tuple
from email.message import EmailMessage

mailUser = "MAIL"
mailPassword = "HASLO OD MAILA"
dataFile = "mail.txt"
jsonFile = "mails.json"
messageFile = "message.txt"
sendingMail = smtplib.SMTP('smtp.gmail.com', 587)


def start():
    print("Starting procedure...")
    print("Loading mails...")
    lista = tuple.createTuple(dataFile)
    print(lista)
    json_data = tuple.convertToJson(lista, jsonFile)
    print(json_data)
    print("Sending mails...")
    # sendMails(mails, messageFile)
    print("Done!")

def generateMessage(file, toMail):
    with open(file) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())
    # from == the sender's email address
    # to == the recipient's email address
    msg['Subject'] = "To jest temat"
    msg['From'] = mailUser
    msg['To'] = toMail
    return msg

def sendMails(mailList, message):
    sendingMail.starttls()
    sendingMail.login(mailUser, mailPassword)

    for mail in mailList:
        try:
            sendingMail.sendmail(mailUser, mail, generateMessage(message, mail).as_string())
        except:
            print(mail)
            print("An error occurred!")

    sendingMail.quit()

if __name__ == "__main__":
    start()