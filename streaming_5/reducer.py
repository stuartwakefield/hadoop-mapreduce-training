#!/bin/env python
import sys

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        # Needs to combine user rows and forum rows
        # First row for a id will be a user followed
        # by all of their posts

if __name__=='__main__':
    reducer()
