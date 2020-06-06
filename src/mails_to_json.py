import json
import re
import uuid


def convert_file_to_dict_list(filename):
    username = None
    user_email = None
    dict_list = []
    pattern_user = re.compile("ytkownik:", re.IGNORECASE)
    pattern_mail = re.compile("mail:", re.IGNORECASE)
    with open(filename, "rt") as file:
        for line in file:
            if pattern_user.search(line):
                username = line.split()[1].split(",")[0]
            elif pattern_mail.search(line):
                user_email = line.split()[1]
            if username and user_email:
                dict_list.append({"Name": username, "Mail": user_email, "UUID": str(uuid.uuid4())})
                username = None
                user_email = None
    return dict_list


def convert_dict_list_to_json(dict_list, filename: str):
    with open(filename, "w") as file:
        json.dump(dict_list, file, indent=2)


def convert_file_to_json(filename, json_filename):
    dictionary_list = convert_file_to_dict_list(filename)
    convert_dict_list_to_json(dictionary_list, json_filename)


if __name__ == "__main__":
    convert_file_to_json("PLIK", "JSON")
