#!/usr/bin/python

import sys

DATA_LENGTH = 2

sales_total = 0
number_of_sales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != DATA_LENGTH:
        continue

    current_sale = data_mapped[1]

    sales_total += float(current_sale)
    number_of_sales +=1

print sales_total, "\t", number_of_sales
