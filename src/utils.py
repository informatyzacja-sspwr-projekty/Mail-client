import datetime
import json
import os
import uuid
from typing import Any

from . import mails_to_json


def clean_logs_and_uuids(config: dict) -> None:
    """Replaces UUID with an empty string for every record in mails.json and cleans logs."""

    file_path = f"data/{config['mails_json_file']}"

    replace_json_property(file_path, 'uuid', '')

    remove_file("logs/sent.log")
    remove_file("logs/notsent.log")


def convert_mails(txt_filename: str, json_filename: str) -> None:
    """Converts mails from txt file to JSON file."""

    mails_to_json.convert_file_to_json(
        f"data/{txt_filename}", f"data/{json_filename}")

    print("E-mails converted!")
    log(f"{current_time()} e-mails converted")


def current_time() -> str:
    """Returns current time."""

    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def generate_uuids(config: dict) -> None:
    """Generates a JSON with new UUIDs for each record in mails.json."""

    file_path = f"data/{config['mails_json_file']}"

    replace_json_property(file_path, 'uuid', str(uuid.uuid4()))


def load_config(filename: str = "config.json") -> list:
    """Returns config file as a list of dictionaries."""

    return read_json(f"config/{filename}")


def log(text: str) -> None:
    """Logs to log file"""

    log_to_file("logs.log", text)


def log_to_file(filename: str, text: str) -> None:
    """Logs to the chosen file"""

    with open(f"logs/{filename}", 'a') as logs:
        logs.write(f"{text}\n")


def read_json(filename: str) -> Any:
    """Reads a JSON file and returns it as a list of dictionaries."""

    try:
        with open(f"{filename}", encoding="utf8") as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file {filename} wasn't found")


def remove_file(filename: str) -> None:
    """Removes file"""
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    except Exception as e:
        raise e


def replace_json_property(filename: str, property: str, to_replace: str) -> None:
    """Replaces all occurrences of property in every record of objects list in json"""

    try:
        mails_json: list = read_json(filename)

        for record in mails_json:
            record[property] = to_replace

        # we don't need to check if file exists - if not then exception is raised by read_json
        with open(filename, mode="w", encoding="utf8") as file:
            json.dump(mails_json, file, indent=2)

    except FileNotFoundError:
        pass


def setup_dirs() -> None:
    """Creates needed dirs if it doesn't exist"""

    os.makedirs("data", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
