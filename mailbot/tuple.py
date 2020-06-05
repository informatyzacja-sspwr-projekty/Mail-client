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
                tupleList.append((userName, userMail, str(uuid.uuid4())))
                userName = None
                userMail = None

    return tupleList


def convertToDict(tuples):
    dict_list = []
    for tuple in tuples:
        dict_list.append({"Name": tuple[0], "Mail": tuple[1], "UUID": tuple[2]})
    return dict_list


def convertToJson(dict_list, fileToWrite: str):
    # dict = {"Accounts": []}
    # for tuple in tupleList:
    #     dict["Accounts"].append(convertToDict(tuple))
    # json_data = json.dumps(dict)
    with open(fileToWrite, "w") as outfile:
        json.dump(dict_list, outfile, indent=2)
    # return json_data


if __name__ == "__main__":
    tuple = createTuple("Ewidencja_adresow_mailowych.txt")
    dictt = convertToDict(tuple)
    jsonn = convertToJson(dictt, "results.json")
