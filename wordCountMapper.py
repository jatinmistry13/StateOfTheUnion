#!/usr/bin/env python

# from http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

import sys
import re
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
	
#def main():
#	filename = "17900108.txt";
#	file = open(filename)
#	htmlData = file.read()
#	strippedHtml = strip_tags(htmlData)
#	strippedHtml = strippedHtml.lstrip()
#	strippedHtml = strippedHtml.rstrip()
#	print strippedHtml
	
	# input comes from STDIN (standard input)
for htmlData in sys.stdin:
    # remove leading and trailing whitespace
    htmlData = htmlData.strip()
    htmlData = htmlData.lower()
    htmlData = strip_tags(htmlData)
    htmlData = re.sub(r'".+"', '', htmlData)
    htmlData = re.sub(r'[^a-zA-Z0-9 ]', '', htmlData)
    # split the line into words
    words = htmlData.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)
