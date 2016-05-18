#!/usr/bin/python

import sys

initialized = False

    #"id"	"title"	"tagnames"	"author_id"	"body"	
    #"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
    #"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"
    #"extra"	"extra_ref_id"	"extra_count"	"marked"

for line in sys.stdin:
    if not initialized:
        initialized = True
        continue
    data = line.strip().replace("\"", "").split("\t")

    if len(data) == 19:
        parent_id = data[7]
        if parent_id=="\N":
            parent_id = data[0]
            item_type = "question"
        else:
            item_type = "answer" 
        length = len(data[4])
        print "{0}\t{1}\t{2}".format(parent_id, item_type, length)

