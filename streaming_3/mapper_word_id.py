#!/bin/env python
import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter="\t")

    for line in reader:
        words = re.findall(r'\w+', line[4])

        for word in words:
            print("%s\t%s" % (word.lower(), line[0]))

if __name__=='__main__':
    mapper()
