#!/usr/bin/python

# date\ttime\tstore name\titem description\tcost\tmethod of payment

import sys

DATA_LENGTH = 6

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == DATA_LENGTH:
        date, time, store, item, cost, payment = data
        print "{0}_{1}\t{2}".format(item, payment, cost)
