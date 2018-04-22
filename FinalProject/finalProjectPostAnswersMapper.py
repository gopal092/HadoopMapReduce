#!/usr/bin/env python
import sys
import csv

csvfile = csv.reader(sys.stdin, delimiter = '\t')

for data in csvfile:
    if(len(data) < 8):
        continue

    nodeType = data[5]
    nodeContent = data[4]

    if(nodeType.strip().lower() == 'question'):
        nodeId = data[0]
        nodeContent = nodeContent.strip()
        questionLength = len(nodeContent)
        print("{0}\t{1}\t{2}".format(nodeId, nodeType, questionLength))
    else:
        parentNodeId = data[6]
        nodeContent = nodeContent.strip()
        answerLength = len(nodeContent)
        print("{0}\t{1}\t{2}".format(parentNodeId, nodeType, answerLength))
