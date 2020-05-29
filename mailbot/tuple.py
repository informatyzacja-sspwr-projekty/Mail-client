# -*- coding: utf-8 -*-
import re
import uuid
import json

def createTuple(filename):
    userName = None
    userMail = None
    tupleList = []
    patternName = re.compile("ytkownik:", re.IGNORECASE)
    patternMail = re.compile("mail:", re.IGNORECASE)
    with open(filename, "rt") as myFile:
        for line in myFile:
            if patternName.search(line) is not None:
                userName = line.split()[1].split(",")[0]
            elif patternMail.search(line) is not None:
                userMail = line.split()[1]

            if userName is not None and userMail is not None:
                tupleList.append((userName, userMail, uuid.uuid4()))
                userName = None
                userMail = None

    return tupleList

def convertToDict(tuple):
    return { "Name": tuple[0], "Mail": tuple[1], "UUID": str(tuple[2])}

def convertToJson(tupleList, fileToWrite):
    dict = {}
    dict['Accounts'] = []
    for tuple in tupleList:
        dict['Accounts'].append(convertToDict(tuple))
    json_data = json.dumps(dict)
    with open(fileToWrite, 'w+') as outfile:
        json.dump(dict, outfile)
    return json_data