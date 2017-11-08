#!/usr/bin/python
import sys

count1 = 0
count2 = 0
count3 = 0

for line in sys.stdin:
    strline = line.strip()

    if "2009" in strline:
        count1 += 1

    if "2010" in strline:
        count2 += 1

    if "2011" in strline:
        count3 += 1

print "2009", count1, "\n", "2010", count2, "\n", "2011", count3
