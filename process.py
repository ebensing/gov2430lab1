#!/usr/bin/python

from os import listdir
from os.path import isfile, join, exists
from collections import defaultdict
import json
import operator
import sys

loc = "."

files = [f for f in listdir(loc) if isfile(join(loc, f)) and "csv" in f ]

counts = defaultdict(int)
userCounts = defaultdict(lambda : defaultdict(int))

if not exists("counts.json") or not exists("userCounts.json"):

  for userFile in files:
    f = open(userFile, 'r')
    print userFile

    for line in f:
      arr = line.split(',')
      name=arr[1]
      words = arr[3].replace("Subject:","").split(" ")
      for w in words:
        counts[w] += 1
        userCounts[name][w] += 1
  
  countsFile=open('counts.json', 'w')
  userCountsFile=open('usercounts.json', 'w')
  countsFile.write(json.dumps(counts))
  userCountsFile.write(json.dumps(userCounts))

else:

  countsFile=open('counts.json', 'r')
  userCountsFile=open('usercounts.json', 'r')

  counts = json.loads(countsFile.read())
  userCounts = json.loads(userCountsFile.read())

if len(sys.argv) <= 1:

  sortedCounts = sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)

  for i in range(0,30):
    print sortedCounts[i]

  scfile = open('sortedCounts.txt', 'w')
  writeStr=""
  for item in sortedCounts:
    writeStr += str(item) + "\n"
  scfile.write(writeStr)

else:

  searchFile = open(sys.argv[1], 'r')
  words = searchFile.read().split('\n')
  words.remove('')
  totalCounts = defaultdict(dict)

  for person, wordCounts in userCounts.iteritems():
    for w in words:
      if w in wordCounts:
        totalCounts[w][person] = wordCounts[w]

  for w in words:
    sortedWords = sorted(totalCounts[w].iteritems(), key=operator.itemgetter(1), reverse=True)
    print w + ":"
    for i in range(0,10):
      print sortedWords[i]

