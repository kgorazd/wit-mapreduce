#!/usr/bin/python

import sys

total_hits = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key = data_mapped[0]

    if old_key and old_key != this_key:
        print old_key, "\t", total_hits
        old_key = this_key;
        total_hits = 0

    old_key = this_key
    total_hits += 1

if old_key != None:
    print old_key, "\t", total_hits

