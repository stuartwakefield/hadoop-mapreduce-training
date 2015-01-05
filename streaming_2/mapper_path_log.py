#!/bin/env python
import sys
import re

log_regexp = r"^(\S+)\s(\S+)\s(\S+)\s\[(\S+\s\S+)\]\s\"([^\"]+)\"\s(\S+)\s(\S+)$"

def mapper():
    for line in sys.stdin:
        matches = re.match(log_regexp, line.strip())
        
        if matches and len(matches.groups()) != 7:
            continue

        ip, identity, username, time, request, status, bytes = matches.groups()
        
        matches = re.match(r"^(\S+)\s(\S+)\s(\S+)$", request)
        
        if matches and len(matches.groups()) != 3:
            continue

        method, path, protocol = matches.groups()
        
        print("%s\t%s" % (path, line.strip()))

if __name__=='__main__':
    mapper()
