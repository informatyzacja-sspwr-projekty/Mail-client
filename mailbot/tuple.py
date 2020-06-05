# -*- coding: utf-8 -*-
import json
import re
import uuid


def createTuple(filename):
    userName = None
    userMail = None
    tupleList = []
    patternName = re.compile("ytkownik:", re.IGNORECASE)
    patternMail = re.compile("mail:", re.IGNORECASE)
    with open(filename, "rt") as myFile:
        for line in myFile:
            if patternName.search(line):
                userName = line.split()[1].split(",")[0]
            elif patternMail.search(line):
                userMail = line.split()[1]

            if userName and userMail:
                tupleList.append((userName, userMail, uuid.uuid4()))
                userName = None
                userMail = None

    return tupleList


def convertToDict(tuple):
    return {"Name": tuple[0], "Mail": tuple[1], "UUID": str(tuple[2])}


def convertToJson(tupleList, fileToWrite: str):
    dict = {"Accounts": []}
    for tuple in tupleList:
        dict["Accounts"].append(convertToDict(tuple))
    json_data = json.dumps(dict)
    with open(fileToWrite, "w+") as outfile:
        json.dump(dict, outfile, indent=2)

    return json_data


if __name__ == "__main__":
    tuple = createTuple("TU WSTAW NAZWE PLIKU")
    dictt = convertToDict(tuple)
    jsonn = convertToJson(dictt, "results.json")
