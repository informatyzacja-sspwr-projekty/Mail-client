import datetime
import json
import os
import uuid


def clean_logs_and_uuids(config: dict):
    """Replaces UUID with an empty string for every record in mails.json and cleans logs."""

    with open(f"data/{config['mails_json_file']}") as mails_json:
        emails_file = json.load(mails_json)
        for record in emails_file:
            record['uuid'] = ''
        json.dump(
            emails_file,
            open(f"data/{config['mails_json_file']}", "w"), indent=2)

    remove_file("logs/sent.log")
    remove_file("logs/notsent.log")


def remove_file(filename: str):
    try:
        os.remove(filename)

    except FileNotFoundError:
        pass

    except Exception as e:
        raise e


def current_time() -> str:
    """Returns current time."""

    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def load_config(filename: str = "config.json"):
    """Returns config file as a list of dictionaries."""

    return read_json(f"config/{filename}")


def log(text: str):
    """Logs to log file"""

    log_to_file("logs.log", text)


def log_to_file(filename: str, text: str):
    """Logs to the chosen file"""

    with open(f"logs/{filename}", 'a') as logs:
        logs.write(f"{text}\n")


def read_json(filename: str):
    """Reads a JSON file and returns it as a list of dictionaries."""

    try:
        with open(f"{filename}", encoding="utf8") as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file {filename} wasn't found")


def setup_dirs():
    """Creates needed dirs if it doesn't exist"""

    try:
        os.makedirs("data")
        os.makedirs("logs")
    except FileExistsError:
        pass


def generate_uuids(config: dict):
    """Generates a JSON with new UUIDs for each record in mails.json."""

    with open(f"data/{config['mails_json_file']}") as file:
        emails_file = json.load(file)
        for record in emails_file:
            record['uuid'] = str(uuid.uuid4())
        json.dump(emails_file, open(f"data/{config['mails_json_file']}", "w"), indent=2)
