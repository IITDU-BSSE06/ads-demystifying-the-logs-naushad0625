#!/usr/bin/python

import sys

count = 0

for line in sys.stdin:
    if line.strip() == "10.99.99.186":
        count = count + 1

print "Total hit made to 10.99.99.186 : ", int(count)
