#!/bin/env python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        # for users add in "A" as the second column
        # for forums make "author_id" (currently the fourth column the first column)
        # and add in "B" as the second column

        # During the shuffle and sort phase we want to ensure the user record
        # is the first row to hit the reducer so that we can add that information
        # into all of the node records. Hence why we have chosen the source identifiers
        # above

if __name__=='__main__':
    mapper()
