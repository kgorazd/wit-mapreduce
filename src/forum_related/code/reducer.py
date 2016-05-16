#!/usr/bin/python

import sys

max_activity_hours = []
current_max = 0
posts = 0
oldKey = None
oldStudent = None

def refreshMax(hour):
    if posts > current_max:
	max_activity_hours = [hour]
    else if posts == current_max:
        max_activity_hours.append[hour]

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, hour, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        #print oldKey, "\t", posts
        oldKey = thisKey;
        posts = 0

    oldKey = thisKey
    posts += 1

if oldKey != None:
    print oldKey, "\t", posts

