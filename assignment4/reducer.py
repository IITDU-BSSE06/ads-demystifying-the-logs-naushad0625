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
        if fileCount > maximumCount:
            maximumCount = fileCount
            maximumCountedFilePath = fileName
        fileName = currentFileName

    fileName = currentFileName
    fileCount += 1

fileArray = maximumCountedFilePath.strip().split("/")
maximumCountedFile = fileArray[len(fileArray)-1]
print "File ", maximumCountedFile, " hitted for ", maximumCount, "times"
