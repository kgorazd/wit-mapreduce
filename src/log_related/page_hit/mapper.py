#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

for line in sys.stdin:
    regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d+) (.*?)'
    data = re.match(regex, line.strip()).groups()
    if len(data) == 7:
        ip, identity, username, endDateTime, request, status, size = data
        print "{0}\t{1}".format(ip, 1)

