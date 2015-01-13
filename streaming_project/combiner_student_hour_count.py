#!/usr/bin/env python
import sys

def combiner():

    last = None
    count = 0

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        user_id, hour = data

        if last and (user_id, hour) != last:
            print('{0}\t{1}\t{2}'.format(last[0], last[1], count))
            count = 0

        last = (user_id, hour)
        count += 1

    if last:
        print('{0}\t{1}\t{2}'.format(last[0], last[1], count))



if __name__ == '__main__':
    combiner()
