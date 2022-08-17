#!/usr/bin/env python3
import json


def main():
    with open("mails.json", "r") as emails_file, open("uuid.txt", "r") as uuids_file, open("confirmed_emails.txt", "w") as confirmed_emails:
        email_json = json.load(emails_file)

        uuids = list(set([el.replace('\n', '')
                     for el in uuids_file.readlines()]))

        for uuid in uuids:
            for record in email_json:
                if record['uuid'] == uuid:
                    confirmed_emails.write(record['mail'] + '\n')


if __name__ == "__main__":
    main()
