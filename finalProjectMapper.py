#!/usr/bin/env python
import sys
import csv

csvfile = csv.reader(sys.stdin, delimiter = '\t')

for data in csvfile:
    #data = line.strip().split('\t')

    #print("Data: {0}\nLength:{1}".format(data,len(data)))
    if(len(data) < 8):
        continue
    author_id = data[3]
    added_date_time = data[8]
    date_time_length = len(added_date_time.split(" "))

    if(date_time_length > 1):
        added_time_hour = added_date_time.split(" ")[1].split(':')[0]
        print("{0}\t{1}".format(author_id, added_time_hour))
