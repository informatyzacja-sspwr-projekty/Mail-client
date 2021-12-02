import datetime
import json


def current_time() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def read_json(filename: str):
    """Reads a JSON file and returns it as a list of dictionaries."""
    try:
        with open(f"{filename}.json", encoding="utf8") as data:
            return json.load(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file {filename} wasn't found")
