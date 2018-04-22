#!/usr/bin/env python
import sys

prevKey = None
prevType = None
prevLength = 0
totalAnsLength = 0
avgAnsLength = 0
totalQuesLength = 0
totalAnswers = 0

for line in sys.stdin:
    data = line.rstrip().split('\t')
    curKey = data[0]
    curLength = data[2]
    curType = data[1]

    if(prevKey != None and prevKey != curKey):
        if(totalQuesLength == 0):
            totalQuesLength = prevLength

        print("{0}\t{1}\t{2}".format(prevKey, totalQuesLength, avgAnsLength))

        if(curType.lower() == 'question'):
            totalQuesLength = int(curLength)
            totalAnswers = 0
        else:
            totalAnsLength = int(curLength)
            totalAnswers = 1

        avgAnsLength = 0

    else:
        if(prevKey == curKey):
            if(curType.lower() == 'question'):
                if(totalAnswers == 0):
                    avgAnsLength = float(totalAnsLength)
                else:
                    avgAnsLength = float(totalAnsLength/totalAnswers)

                totalQuesLength = curLength
                totalAnsLength = 0

            else:
                totalAnsLength += int(curLength)
                totalAnswers = totalAnswers + 1

    prevKey = curKey
    prevLength = curLength

if(prevKey != None):
    if(curType.lower() == 'question'):
        if(totalQuesLength == 0):
            totalQuesLength = prevLength
        print("{0}\t{1}\t{2}".format(prevKey, totalQuesLength, avgAnsLength))
