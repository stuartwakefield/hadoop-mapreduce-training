#!/usr/bin/env python
import sys

def reducer():

    last = None
    counts = dict()
    
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 3:
            continue

        user_id, hour, count = data

        if last and user_id != last:
            hours = counts.items()
            hours.sort(key=lambda x: x[1])
            last_hour, last_count = hours.pop(0)
            print('{0}\t{1}\t{2}'.format(last, last_hour, last_count))
            counts = dict()

        last = user_id

        if not hour in counts:
            counts[hour] = int(count)
        else:
            counts[hour] += int(count)

    if last:
        hours = counts.items()
        hours.sort(key=lambda x: x[1])
        last_hour, last_count = hours.pop(0)
        print('{0}\t{1}\t{2}'.format(last, last_hour, last_count))

if __name__ == '__main__':
    reducer()
