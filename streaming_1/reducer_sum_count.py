#!/bin/env python
import sys
from decimal import *

def reducer():

    total = 0
    count = 0
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, amount = data

        if last and key != last:
            print("%s\t%s\t%s" % (last, total, count))
            total = 0
            count = 0

        total += Decimal(amount)
        count += 1
        last = key

    if last:
        print("%s\t%s\t%s" % (last, total, count))

if __name__=='__main__':
    reducer()
