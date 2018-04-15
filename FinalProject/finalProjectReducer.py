#!/usr/bin/env python
import sys

prevKey = None
prevValue = None
postCount = 0
maxPostCount = 0
maxKey = ""
maxHour = ""
multipleMaxElements = ""


for line in sys.stdin:
    data = line.strip().split('\t')

    curKey = data[0]
    curValue = data[1]

    #print("{0}\t{1}".format(curKey, curValue))
    if(prevKey != None and prevKey != curKey):
        print ("{0}".format(multipleMaxElements))
        multipleMaxElements = ""
        maxPostCount = 1
        postCount = 1
        maxKey = curKey
        maxHour = curValue

    else:
        if(prevKey == curKey):
            if(prevValue == curValue):
                postCount += 1
            else:
                if(postCount > maxPostCount):
                    maxPostCount = postCount
                    maxKey = curKey
                    maxHour = curValue

                postCount = 1

                if(postCount == maxPostCount):
                    multipleMaxElements += curKey + "\t" + curValue + "\n"

        else:
            if(postCount >= maxPostCount):
                maxPostCount = postCount
                maxKey = curKey
                maxHour = curValue
                postCount = 1

    if(postCount > maxPostCount):
        multipleMaxElements = ""
        maxPostCount = postCount

    if(multipleMaxElements == ""):
        multipleMaxElements += curKey + "\t" + curValue + "\n"

    prevKey = curKey
    prevValue = curValue

if(prevKey != None):
    if(postCount > maxPostCount):
        multipleMaxElements = ""

    print ("{0}".format(multipleMaxElements))
