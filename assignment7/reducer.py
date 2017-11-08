#!/usr/bin/python

import sys

getCount = 0
postCount = 0
headCount = 0


for line in sys.stdin:

    if "GET" in line.strip() :
        getCount += 1
    elif "POST" in line.strip():
        postCount +=1
    elif "HEAD" in line.strip():
        headCount +=1
    

print "GET", getCount, "\n", "POST", postCount, "HEAD", headCount
