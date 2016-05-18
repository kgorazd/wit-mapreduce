#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    regex = '([(\d\.)]+) (.*?) (.*?) \[(.*?)\] "(.*?)" (\d+) (.*?)'
    data = re.match(regex, line.strip()).groups()
    if len(data) == 7:
        ip, identity, username, endDateTime, request, status, size = data
        if request.endswith("/"):
        	request = request[:-1]
        print "{0}\t{1}".format(request, 1)

