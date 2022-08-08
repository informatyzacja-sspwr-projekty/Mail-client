import json

emails_file = open("mails.json", "r")
uuids_file = open("uuid.txt", "r")
emails = open("emails.txt", "w")

email_uuid_json = json.load(emails_file)
uuid_lines = [el.replace('\n', '') for el in uuids_file.readlines()]
email_uuid_lines = [record['uuid'] for record in email_uuid_json]

uuid_lines.sort()
email_uuid_lines.sort()

for record in email_uuid_json:
    for uuid in email_uuid_lines:
        if record['uuid'] == uuid:
            emails.write(record['mail'] + '\n')

emails_file.close()
uuids_file.close()
