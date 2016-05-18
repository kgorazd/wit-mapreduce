#!/usr/bin/python

import sys

maxActivityHours = []
currentMax = 0
posts = 0
oldKey = None
authorId = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey = data_mapped[0]
    authorId, hour = thisKey.split("_")

    if authorId and authorId != thisKey:
        print authorId, "\t", maxActivityHours
        oldKey = thisKey;
        posts = 0

    oldKey = thisKey
    posts += 1
    if posts == currentMax:
        currentMax = posts
        maxActivityHours.append(hour)
    elif posts > currentMax:
        currentMax = posts
        maxActivityHours = [hour]

if authorId != None:
    print authorId, "\t", maxActivityHours

