#!/bin/env python
import sys

def reducer():

    count = 0
    node_ids = []
    last = None

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        key, node_id = data

        if last and key != last:
            node_ids.sort()
            print("%s\t%s\t%s" % (last, count, ",".join(str(node_id) for node_id in node_ids)))
            count = 0
            node_ids = []

        count += 1
        node_ids.append(int(node_id))
        last = key

    if last:
        node_ids.sort()
        print("%s\t%s\t%s" % (last, count, ",".join(str(node_id) for node_id in node_ids)))

if __name__=='__main__':
    reducer()
