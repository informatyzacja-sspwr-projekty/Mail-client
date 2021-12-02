import datetime
import json


def current_time() -> str:
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def read_json(filename: str):
    """Reads a JSON file and returns it as a list of dictionaries."""
    with open(filename) as file:
        data = json.load(file)
    return data
