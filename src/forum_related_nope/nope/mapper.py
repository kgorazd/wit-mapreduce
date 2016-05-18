#!/usr/bin/python

#"id"	"title"	"tagnames"	"author_id"	"body"	
#"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"	
#"state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"
#"extra"	"extra_ref_id"	"extra_count"	"marked"

import sys

initialized = False

for line in sys.stdin:
    if not initialized:
        initialized = True
        continue
    data = line.strip().split("\t")
    if len(data) == 19:
        author_id = data[3].replace("\"","")
        added_at = data[8]
        hour_only = added_at[12:14]
        print "{0}_{1}\t{2}".format(author_id, hour_only, 1)

