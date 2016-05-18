#!/usr/bin/python

import sys

DATA_LENGTH = 2

sales_total = 0
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != DATA_LENGTH:
        continue

    current_key, current_sale = data_mapped

    if old_key and old_key != current_key:
        print old_key, "\t", sales_total
        old_key = current_key
        sales_total = 0

    old_key = current_key
    sales_total += float(current_sale)

if old_key != None:
    print old_key, "\t", sales_total
