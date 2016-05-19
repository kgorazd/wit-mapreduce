#!/usr/bin/python

import sys

current_count = 0
old_key = None
max_count = -1
max_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key = data_mapped[0]

    if old_key and old_key != this_key:
        old_key = this_key;
        current_count = 0

    old_key = this_key
    current_count += 1
    if current_count > max_count:
        max_count = current_count
        max_key = this_key

if old_key != None:
    print max_key, "\t", max_count

