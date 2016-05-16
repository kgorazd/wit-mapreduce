#!/usr/bin/python

import sys

initialized = False

for line in sys.stdin:
    if not initialized:
        initialized = True
        continue
    data = line.strip().replace("\"", "").split("\t")
    #"id"	"title"	"tagnames"	"author_id"	"body"	
    #"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
    #"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"
    #"extra"	"extra_ref_id"	"extra_count"	"marked"
    #19
    if len(data) == 19:
        parent_id = data[7]
        row_type = "answer" 
        if parent_id=="\N":
            parent_id = data[0]
            row_type = "question"
        length = len(data[4])
        print "{0}\t{1}\t{2}".format(parent_id, row_type, length)

