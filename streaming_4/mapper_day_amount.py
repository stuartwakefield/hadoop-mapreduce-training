#!/bin/env python
from datetime import datetime
import csv
import sys

def mapper():
    reader = csv.reader(sys.stdin, delimiter="\t")

    for line in reader:

        day = datetime.strptime(line[0], "%Y-%m-%d").weekday()
        amount = line[4]

        print("{0}\t{1}".format(day, amount))

if __name__=="__main__":
    mapper()
