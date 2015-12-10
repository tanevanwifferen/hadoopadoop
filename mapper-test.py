#!/usr/bin/env python

import sys
import csv
from langdetect import detect

def mapper():
  reader = csv.reader(x.replace('\0','').replace('\n','').replace('\r','') for $

  for line in reader:
    words = line[4].strip() # get tweet text
    if words != 'TEXT': # ignore csv header
      try:
        if detect(unicode(words, "utf8")) == 'en':
          print words
      except Exception:
        pass # ignore tweets that don't contain actual words

