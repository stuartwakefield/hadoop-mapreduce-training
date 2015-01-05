#!/bin/env python
import sys

def reducer():

    result = 0
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, value = data

        count = int(value)

        if count > result:
            result = count
            last = key

    if last:
        print("%s\t%s" % (last, result))

if __name__=='__main__':
    reducer()
