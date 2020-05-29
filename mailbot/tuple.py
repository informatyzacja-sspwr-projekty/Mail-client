# -*- coding: utf-8 -*-
import re
import uuid

def createTuple(filename):
    userName = ""
    userMail = ""
    tupleList = []
    patternName = re.compile("ytkownik:", re.IGNORECASE)
    patternMail = re.compile("mail:", re.IGNORECASE)
    with open(filename, "rt") as myFile:
        for line in myFile:

            if patternName.search(line) is not None:
                user1 = line.split(" ")
                user2 = user1[1].split(",")
                userName = user2[0]

            if patternMail.search(line) is not None:
                mail = line.split(" ")
                userMail = mail[1]
                print(userMail)
            tupleList.append((userName, userMail, uuid.uuid4()))
    return tupleList
