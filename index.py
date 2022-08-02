#!/usr/bin/env python3
from src import mail_sender, mails_to_json, utils
from src.mail_receiver import MailReceiver
from os.path import exists


def convert_mails(txt_filename: str, json_filename: str):
    """Converts mails from txt file to JSON file."""

    mails_to_json.convert_file_to_json(
        f"data/{txt_filename}", f"data/{json_filename}")

    print("Mails converted!")
    utils.log(f"{utils.current_time()} Mails converted")


def send_mails(config: dict):
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
                print("No new mails have been sent!")
                utils.log(f"{utils.current_time()} No new mails sent")
                return
    mail_receivers = map(lambda x: MailReceiver(x), users_data)
    mail_sender.send_mails(config, mail_receivers)
    print("Mails have been sent!")
    utils.log(f"{utils.current_time()} Mails sent")


def send_mail_with_attachments(config: dict):
    """Sends mail with results of bot usage to original sender"""

    mail_sender.send_mail_with_attachments(config)

    print("Mail with attachments have been sent!")
    utils.log(f"{utils.current_time()} Mail with attachments sent")


if __name__ == "__main__":
    config = utils.load_config()

    utils.setup_dirs()
    #utils.clear_logs()

    convert_mails(config["mails_txt_file"], config["mails_json_file"])
    send_mails(config)
    send_mail_with_attachments(config)
