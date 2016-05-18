#!/usr/bin/python

import sys

oldKey = None
question_length = 0
answer_length_sum = 0
answer_count = 0

def resetCounters():
    answer_length_sum = 0
    answer_count = 0

def updateResults():
    print oldKey, "\t", question_length, "\t", averageAnswerCount()

def averageAnswerCount():
    if answer_count==0:
        return 0
    return answer_length_sum / answer_count

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisKey, itemType, length = data_mapped

    if oldKey and oldKey != thisKey:
        updateResults()
        oldKey = thisKey
        resetCounters()

    oldKey = thisKey
    if itemType == "question":
        question_length = length
    else:
        answer_length_sum += float(length)
        answer_count += 1

if oldKey != None:
    updateResults()

