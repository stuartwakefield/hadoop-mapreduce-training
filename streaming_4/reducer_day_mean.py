#!/bin/env python
import sys
from decimal import *

def reducer():

    last = None
    count = 0
    total = 0

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        day, amount = data

        if last and last != day:
            print("{0}\t{1}".format(last, str(total / count)))
            count = 0
            total = 0

        last = day
        count += 1
        total += Decimal(amount)

    print("{0}\t{1}".format(last, str(total / count)))

if __name__=="__main__":
    reducer()
