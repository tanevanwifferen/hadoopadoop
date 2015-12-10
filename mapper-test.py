#!/usr/bin/env python

import sys
import csv

def mapper():
  reader = csv.reader(x.replace('\0','').replace('\n','').replace('\r','') for x in sys.stdin)

  for line in reader:
    words = line[4].strip() # get tweet text
    if words != 'TEXT': # ignore csv header
      print words
