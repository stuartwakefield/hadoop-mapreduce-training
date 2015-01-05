#!/bin/env python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue

        date, time, store, category, amount, type = data

        print("%s\t%s" % (category, amount))

if __name__=='__main__':
    mapper()
