#!/usr/bin/env python

from operator import itemgetter
import sys
import math

current_word = None
current_count = 0
word = None

wordcount = {}
count_list = []

wordcountByFile = {}
extrawordcount = {}
wordAvg = {}
wordStdDev = {}

def addToDictionary(current_word, current_count):
    wordkey = current_word.split("_")[0]
    if wordcount.get(wordkey) == None:
        count_list = []
        count_list.append(current_count)
        wordcount[wordkey] = count_list
    else:
        wordcount.get(wordkey).append(current_count)

def addToDictByFile(current_word):
    if wordcountByFile.get(current_word) == None:
        wordcountByFile[current_word] = 1
    else:
        count_val = wordcountByFile.get(current_word)
        wordcountByFile[current_word] = count_val + 1

def addToWordCount(current_word):
    if wordcount.get(current_word) == None:
        wordcount[current_word] = 1
    else:
        count_val = wordcount.get(current_word)
        wordcount[current_word] = count_val + 1

def addToExtraWordCount(word):
    if extrawordcount.get(word) == None:
        extrawordcount[word] = 1
    else:
        extrawordcount[word] = extrawordcount[word] + 1

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
        
def calculateAverage():
    average = -1
    for word in wordcount:
        average = sum(wordcount.get(word))/5.0
    return average

def calculateStdDev():
    stdDev = -1
    average = -1
    for word in wordcount:
        partialSquare = -1
        sumOfSquare = -1
        average = sum(wordcount.get(word))/5.0
        countlist = wordcount.get(word)
        for count in countlist:
            partialSquare = (count-average)**2
            sumOfSquare += partialSquare
        stdDev = math.sqrt(sumOfSquare/5.0)
        print '%s\t%s\t%s' % (word, average, stdDev)

#def slicedict(d, s):
#    return {k:v for k,v in d.iteritems() if k.startswith(s)}
def slicedict(sourcedict, string):
    #print sourcedict
    #print string
    newdict = {}
    for key in sourcedict.keys():
        if key.startswith(string):
            newdict[key] = sourcedict[key]
    return newdict

def calculateStdDev2():
    #stdDev = 0
    average = 0
    for word in wordcount:
        #print word
        #print "WordAverageWondow: " + word + "\t" + "wordcount: " + str(wordcount.get(word)) + "avg: " + "\t" + str(average)
        average = (wordcount.get(word)/5.0)
        #print "WordAverageWondow: " + word + "\t" + "wordcount: " + str(wordcount.get(word)) + "avg: " + "\t" + str(average)
        partialSquare = 0
        sumOfSquare = 0
        stdDev = 0
        tempdict = slicedict(wordcountByFile, word+"_")
        #print tempdict
        for tempkey in tempdict:
            partialSquare = (int(tempdict.get(tempkey))-average)*(int(tempdict.get(tempkey))-average)
            #print partialSquare
            sumOfSquare += partialSquare
        stdDev = math.sqrt(sumOfSquare/5.0)
        #print "WordAverageWondow: " + word + "\t" + str(average)
        wordAvg[word] = average
        wordStdDev[word] = stdDev
        #print '%s\t%s\t%s' % (word, average, stdDev)

def calculateTwoStdDev():
    calculateStdDev2()
    for word in wordcount:
        if wordAvg.get(word) == None or wordStdDev.get(word) == None:
            continue
        nWordAverage = wordAvg.get(word)
        nWordStdDev = wordStdDev.get(word)
        nTwoStdDev = nWordAverage + 2*nWordStdDev
        nExtraWordCount = extrawordcount.get(word)
        if nExtraWordCount == None:
            continue
        elif nExtraWordCount > nTwoStdDev:
            print '%s\t%s\t%s\t%s\t%s' % (word, nExtraWordCount, nWordAverage, nWordStdDev, nTwoStdDev) 
    

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    
    dict_word = ""
    dic_count = ""
    # convert count (currently a string) to int
    try:
        dict_word = word + "_" + count.split("_")[1]
        dic_count = count.split("_")[0]
        dic_count = int(dic_count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if "_file6" in dict_word:
        addToExtraWordCount(word)
    else:
        addToDictByFile(dict_word)
        addToWordCount(word)

#calculateStdDev2()
calculateTwoStdDev()


'''
    # convert count (currently a string) to int
    try:
        word = word + count.split("_")[1]
        count = count.split("_")[0]
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
'''

#calculateStdDev(calculateAverage())
