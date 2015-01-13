#!/bin/env python
import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    last = None
    user = None

    writer.writerow([
        "user_ptr_id", "reputation", "gold", "silver", "bronze",
        "id", "title", "tagnames", "body", "node_type", "parent_id",
        "abs_parent_id", "added_at", "score", "state_string",
        "last_edited_id", "last_activity_by_id", "last_activity_at",
        "active_revision_id", "extra", "extra_ref_id", "extra_count", "marked"
    ])

    for line in reader:

        if len(line) == 20:
            user_id = line[0]
            if user_id == last:
                writer.writerow(user[0:1] + user[2:] + line[2:])

        if len(line) == 6:
            user = line
            last = user[0]

if __name__=='__main__':
    reducer()
