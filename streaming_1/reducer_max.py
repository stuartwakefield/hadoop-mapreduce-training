#!/bin/env python
import sys
from decimal import *

def reducer():

    result = 0
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, amount = data

        if last and key != last:
            print("%s\t%s" % (last, result))
            result = 0

        result = max(Decimal(amount), result)
        last = key

    if last:
        print("%s\t%s" % (last, result))

if __name__=='__main__':
    reducer()
