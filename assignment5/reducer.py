#!/usr/bin/python


import sys

fileName = None
maximumCount = 0
fileCount = 0
maximumCountedFile = None
maximumCountedFilePath = None

for line in sys.stdin:

    currentFileName = line.strip()

    if "?" in currentFileName:
        currentFileNameArray = currentFileName.strip().split("?")
        currentFileName = currentFileNameArray[0]

    if fileName and currentFileName != fileName:
        fileCount += 1
        fileName = currentFileName

    fileName = currentFileName

print "Number of unique files: ", fileCount
