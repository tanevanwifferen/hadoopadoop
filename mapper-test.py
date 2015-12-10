#!/usr/bin/env python

import sys
import csv
from langdetect import detect

reader = csv.reader(x.replace('\0','').replace('\n','').replace('\r','') for x in sys.stdin)

for line in reader:
  # remove leading and trailing whitespace
  line = line[4].strip() # get tweet text
  # ingore header
  if line != 'TEXT': # ignore csv header
    try:
      # check if tweet is written in English
      if detect(unicode(line, "utf8")) == 'en':
        # split the line into words
        words = line.split()
        for word in words:
          print '%s\t%s' % (word, 1)
    except Exception:
      pass # ignore tweets that don't contain actual words
