#!/bin/env python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        
        if len(line) == 19:
            user_id = line[3]
            body = re.sub(r'[\s]+', ' ', line[4])

            if user_id == "author_id":
                continue

            writer.writerow([user_id, "B"] + line[:3] + [body] + line[5:])

        elif len(line) == 5:
            user_id = line[0]

            if user_id == "user_ptr_id":
                continue

            writer.writerow([user_id, "A"] + line[1:])

        else:
            continue

if __name__=='__main__':
    mapper()
