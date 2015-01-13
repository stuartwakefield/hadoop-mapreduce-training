#!/bin/env python
import sys
from decimal import *

def reducer():

    last = None
    total_count = 0
    total_amount = 0

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) == 2:
            day, amount = data
            count = 1

        elif len(data) == 3:
            day, avg, count = data
            count = int(count)
            amount = Decimal(avg) * count

        else:
            continue

        if last and last != day:
            print("{0}\t{1}\t{2}".format(last, str(total_amount / total_count), str(total_count)))
            count = 0
            total = 0

        last = day
        total_count += count
        total_amount += Decimal(amount)

    if last:
        print("{0}\t{1}\t{2}".format(last, str(total_amount / total_count), str(total_count)))

if __name__=="__main__":
    reducer()
