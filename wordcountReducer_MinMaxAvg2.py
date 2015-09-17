#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

wordcount = {}
count_list = []

def addToDictionary(current_word, current_count):
    wordkey = current_word.split("_")[0]
    if wordcount.get(wordkey) == None:
        count_list = []
        count_list.append(current_count)
        wordcount[wordkey] = count_list
    else:
        wordcount.get(wordkey).append(current_count)


def calculateMinMaxAvg():
    average = -1
    minimum = -1
    maximum = -1
    for word in wordcount:
        #print wordcount.get(word)
        minimum = min(wordcount.get(word))
        maximum = max(wordcount.get(word))
        average = sum(wordcount.get(word))/229.0
        print '%s\t%s\t%s\t%s' % (word, minimum, maximum, average)

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            #print '%s\t%s' % (current_word, current_count)
            addToDictionary(current_word, current_count)
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    #print '%s\t%s' % (current_word, current_count)
    addToDictionary(current_word, current_count)


calculateMinMaxAvg()
