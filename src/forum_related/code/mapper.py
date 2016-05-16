#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

initialized = False

for line in sys.stdin:
    if not initialized:
	initialized = True
        continue
    data = line.strip().split("\t")
    #"id"	"title"	"tagnames"	"author_id"	"body"	
    #"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
    #"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"
    #"extra"	"extra_ref_id"	"extra_count"	"marked"
    #19
    #3
    #8
    if len(data) == 19:
        # date, time, store, item, cost, payment = data
        author_id = data[3][1:-1]
        added_at = data[8]
        hour_only = added_at[12:14]
        print "{0}_{1}\t{2}".format(author_id, hour_only, 1)

