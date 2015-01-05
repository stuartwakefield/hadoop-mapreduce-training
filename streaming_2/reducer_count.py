#!/bin/env python
import sys

def reducer():

    count = 0
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, value = data

        if last and key != last:
            print("%s\t%s" % (last, count))
            count = 0

        count += 1
        last = key

    if last:
        print("%s\t%s" % (last, count))

if __name__=='__main__':
    reducer()
