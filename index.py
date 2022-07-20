#!/usr/bin/env python3
import sys

from src import mail_sender, mails_to_json, utils
from src.mail_receiver import MailReceiver
import argparse
import json
import uuid
import os


def convert_mails(txt_filename: str, json_filename: str):
    """Converts mails from txt file to JSON file."""

    mails_to_json.convert_file_to_json(
        f"data/{txt_filename}", f"data/{json_filename}")

    print("Mails converted!")
    utils.log(f"{utils.current_time()} Mails converted")


def send_mails(config: dict):
    """Prepares users' data and sends mails to receivers."""

    users_data = utils.read_json(f"data/{config['mails_json_file']}")
    mail_receivers = map(lambda x: MailReceiver(x), users_data)

    mail_sender.send_mails(config, mail_receivers)

    print("Mails have been sent!")
    utils.log(f"{utils.current_time()} Mails sent")


def send_mail_with_attachments(config: dict):
    """Sends mail with results of bot usage to original sender"""

    mail_sender.send_mail_with_attachments(config)

    print("Mail with attachments have been sent!")
    utils.log(f"{utils.current_time()} Mail with attachments sent")


def clear_uuids_and_logs():
    """Replaces UUID with an empty string for every record in mails.json and clears logs."""

    with open("data/mails.json") as mails_json:
        emails_file = json.load(mails_json)
        for record in emails_file:
            record['uuid'] = ''
        json.dump(emails_file, open("data/mails.json", "w"), indent=2)

    # clear logs
    with open("logs/sent.log") as logs:
        pass

    if os.path.exists("logs/sent.log"):
        with open("logs/notsent.log") as logs:
            pass


def generate_uuids():
    """Generates a JSON with new UUIDs for each record in mails.json."""

    with open("data/mails.json") as file:
        emails_file = json.load(file)
        for record in emails_file:
            record['uuid'] = str(uuid.uuid4())
        json.dump(emails_file, open("data/mails.json", "w"), indent=2)


def send_emails():
    """Sends e-mails, skips those addresses which already received a message."""

    # Skip email addresses which already received a message:
    if os.path.exists("logs/sent.log") and os.path.getsize("logs/sent.log") > 0:
        with open("logs/sent.log", "r") as sent_list:
            handled_email_addresses = [email.replace('\n', '') for email in sent_list.readlines()]

        with open("data/mails.json") as emails_json:
            emails_file = json.load(emails_json)
            for email in handled_email_addresses:
                for record in emails_file:
                    if record['mail'] == email:
                        emails_file.remove(record)
            json.dump(emails_file, open("data/mails.json", "w"), indent=2)

    # Send emails:
    if os.path.getsize("data/mails.json") > 0:
        config = utils.load_config()

        utils.setup_dirs()
        # utils.clear_logs()

        convert_mails(config["mails_txt_file"], config["mails_json_file"])
        send_mails(config)
        send_mail_with_attachments(config)


def main():
    parser = argparse.ArgumentParser(description='Handles sending emails')

    parser.add_argument('-c', '--clear', dest='clear', action='store_true',
                        help='clear UUIDs of the handled e-mail addresses')
    parser.add_argument('-g', '--generate', dest='generate', action='store_true',
                        help='generate new UUIDs for each e-mail account')
    parser.add_argument('-s', '--send', dest='send', action='store_true', help='send a message for each e-mail account')

    args = parser.parse_args()

    if args.clear:
        clear_uuids_and_logs()
        if sys.argv[-1] == '-c' or sys.argv[-1] == '--clear':
            print("All UUIDs cleaned")

    elif args.generate:
        generate_uuids()
        if sys.argv[-1] == '-g' or sys.argv[-1] == '--generate':
            print("New UUIDs generated")

    elif args.send:
        send_emails()
        if sys.argv[-1] == '-s' or sys.argv[-1] == '--send':
            print("E-mails sent")

    else:
        parser.parse_args(['-h'])


if __name__ == "__main__":
    main()
