import json
import re
import uuid


def convert_file_to_dict_list(filename: str) -> list:
    """Converts a file with users and email addresses given in (data/)file named from mails_txt_file property
    from config file into a list of dictionaries, where each dictionary is a separate email."""
    username = None
    email = None
    users_data = []
    pattern_user = re.compile("user:", re.IGNORECASE)
    pattern_mail = re.compile("mail:", re.IGNORECASE)
    try:
        with open(filename, "rt") as file:
            for line in file:
                if pattern_user.search(line):
                    username = line.split()[1].split(",")[0]
                elif pattern_mail.search(line):
                    email = line.split()[1]
                if username and email:
                    users_data.append(
                        {"name": username, "mail": email, "uuid": str(uuid.uuid4())})
                    username = None
                    email = None
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} wasn't found")

    return users_data


def convert_dict_list_to_json(users_data: list, filename: str):
    """Converts a list of dictionaries into a JSON file."""
    with open(filename, "w") as file:
        json.dump(users_data, file, indent=2)


def convert_file_to_json(filename: str, json_filename: str):
    """Converts a file with users and email addresses into a JSON file."""
    users_data = convert_file_to_dict_list(filename)
    convert_dict_list_to_json(users_data, json_filename)
