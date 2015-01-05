#!/bin/env python
import sys
from decimal import *

def reducer():

    total = 0
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, amount = data

        if last and key != last:
            print("%s\t%s" % (last, total))
            total = 0

        total += Decimal(amount)
        last = key

    if last:
        print("%s\t%s" % (last, total))

if __name__=='__main__':
    reducer()
