#!/usr/bin/env python3
import argparse
import os
from os.path import exists

from src import mail_sender, utils


def send_mails(config: dict) -> None:
    """Prepares users' data and sends mails to receivers."""

    users_data = utils.read_json(f"data/{config['mails_json_file']}")

    if exists(f"logs/sent.log"):
        all_mails = [sub['mail'] for sub in users_data]

        with open(f"logs/sent.log") as file:
            log_mails = file.readlines()
            sent_mails = [line.rstrip() for line in log_mails]
            diff = list(set(all_mails) - set(sent_mails))

            if diff:
                users_data = [x for x in users_data if x['mail'] in diff]
            else:
                print("No new e-mails have been sent!")
                utils.log(f"{utils.current_time()} No new e-mails sent")

                return

    mail_sender.send_mails(config, users_data)

    print("E-mails have been sent!")
    utils.log(f"{utils.current_time()} e-mails sent")


def send_mail_with_attachments(config: dict) -> None:
    """Sends mail with results of bot usage to original sender"""

    mail_sender.send_mail_with_attachments(config)

    print("E-mails with attachments have been sent!")
    utils.log(f"{utils.current_time()} e-mail with attachments sent")


def send_emails(config: dict) -> None:
    """Sends e-mails, skips those addresses which already received a message."""

    # Send emails:
    if os.path.getsize(f"data/{config['mails_json_file']}") > 0:
        send_mails(config)
        send_mail_with_attachments(config)


def main() -> None:
    config = utils.load_config()

    utils.setup_dirs()

    parser = argparse.ArgumentParser(description='Handles sending emails')

    parser.add_argument('-c', '--clean', dest='clean', action='store_true',
                        help='clean logs and UUIDs of the handled e-mail addresses')
    parser.add_argument('-g', '--generate', dest='generate', action='store_true',
                        help='generate new UUIDs for each e-mail account')
    parser.add_argument('-s', '--send', dest='send', action='store_true', help='send a message for each e-mail account')

    args = parser.parse_args()

    if args.clean:
        utils.clean_logs_and_uuids(config)
        print("Logs and UUIDs cleaned")

    elif args.generate:
        utils.convert_mails(config["mails_txt_file"], config["mails_json_file"])
        utils.generate_uuids(config)
        print("New UUIDs generated")

    elif args.send:
        send_emails(config)
        print("E-mails have been sent!")

    else:
        parser.parse_args(['-h'])


if __name__ == "__main__":
    main()
