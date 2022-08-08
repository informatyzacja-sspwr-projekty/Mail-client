import json

with open("mails.json", "r") as emails_file, open("uuid.txt", "r") as uuids_file, open("emails.txt", "w") as emails:
    email_uuid_json = json.load(emails_file)
    uuid_lines = list(set([el.replace('\n', '') for el in uuids_file.readlines()]))
    email_uuid_lines = [record['uuid'] for record in email_uuid_json]

    for uuid in email_uuid_lines:
        for record in email_uuid_json:
            if record['uuid'] == uuid:
                emails.write(record['mail'] + '\n')
