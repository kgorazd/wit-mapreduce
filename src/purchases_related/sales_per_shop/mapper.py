#!/usr/bin/python

# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

DATA_LENGTH = 6

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)
