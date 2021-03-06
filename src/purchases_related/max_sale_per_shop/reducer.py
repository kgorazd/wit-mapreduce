#!/usr/bin/python

import sys

max_sale = -1
old_key = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    current_key, current_sale = data_mapped

    if old_key and old_key != current_key:
        print old_key, "\t", max_sale
        old_key = current_key
        max_sale = -1

    old_key = current_key
    current_sale=float(current_sale)
    if max_sale < current_sale:
        max_sale = current_sale

if old_key != None:
    print old_key, "\t", max_sale

