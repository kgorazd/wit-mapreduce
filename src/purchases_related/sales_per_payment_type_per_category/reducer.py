#!/usr/bin/python

import sys

DATA_LENGTH = 2

total_sales = -1
old_key = None

def print_to_result():
    category, payment = old_key.split("_")
    print category, "\t", payment, "\t", total_sales

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != DATA_LENGTH:
        continue

    current_key, current_sale = data_mapped

    if old_key and old_key != current_key:
        print_to_result()
        old_key = current_key
        total_sales = 0

    old_key = current_key
    total_sales += float(current_sale)

if old_key != None:
    print_to_result()
