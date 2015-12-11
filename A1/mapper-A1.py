#!/usr/bin/env python

import sys
import csv
from langdetect import detect

# get arguments
start = sys.argv[1]+':00:00'
end = sys.argv[2]+':00:00'

reader = csv.reader(x.replace('\0','').replace('\n','').replace('\r','') for x $

for line in reader:

  # remove leading and trailing whitespace
  text = line[4].strip() # get tweet text
  date = line[5].strip() # get tweet created

  # skip if tweet does not fall within time range
  if text != 'TEXT': # ignore csv header:
    if date[11:] < start or date[11:] > end:
      continue

  # ingore header
  if text != 'TEXT': # ignore csv header
    try:
      # split the line into words
      words = text.split()
      for word in words:
        if word.startswith("#"):
          print '%s\t%s' % (word, 1)
    except Exception:
      pass # ignore tweets that don't contain actual words
