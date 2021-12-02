import datetime
import json


def current_time() -> str:
    """Returns current time."""
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def load_config(filename: str = "config/config.json"):
    """Returns config file as a list of dictionaries."""
    return read_json(filename)[0]  # [0] to get the dict


def log(text: str):
    """Logs to log file"""
    with open("logs/logs.log", 'a') as logs:
        logs.write(text)


def read_json(filename: str):
    """Reads a JSON file and returns it as a list of dictionaries."""
    try:
        with open(f"{filename}", encoding="utf8") as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file {filename} wasn't found")
