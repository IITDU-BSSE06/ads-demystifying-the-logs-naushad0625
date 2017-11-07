#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
    if "/assets/js/the-associates.js" in line:
        count += 1

print "Number of hits were made to /assets/js/the-associates.js: ", count
