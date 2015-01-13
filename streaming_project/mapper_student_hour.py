#!/usr/bin/env python
import csv
import sys
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    
    for line in reader:
        user_id = line[3]

        if user_id == 'author_id':
            continue

        added_at_hour = datetime.strptime(line[8][0:-3], "%Y-%m-%d %H:%M:%S.%f").hour

        print("{0}\t{1}".format(user_id, added_at_hour))

if __name__ == '__main__':
    mapper()
