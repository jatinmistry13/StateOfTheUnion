# StateOfTheUnion
This is a repository for my CS757 - Mining massive datasets assignment 1 - State of the Union dataset (SOTU)

First just download all the html files from the website : 
These html files contain the State of the Union address from US presidents.

### 1. Introduction:

This assignment consists of using the WordCount program in Hadoop and modifying it to do several tasks. The data you will use are the text transcriptions of the State of the Union Addresses given by Presidents to Congress since 1790 to the present year.

The data consists of files named yyyymmdd.txt, where yyyy is the year, mm the month, and dd the day in which the address was given

As it stands, the files contain html commands and other characters (one of your jobs will be to eliminate those)

The data can be found in: [State of the Union Website](http://stateoftheunion.onetwothree.net/texts/index.html)

### 2. Tasks:

Run the version of WordCount found in Hadoop in Distributed mode. Obtain a graph that shows the running time vs. the size of the file (for this you would have to run WordCount several times, using incrementally larger data sizes - by using more and more files-)
- Keep in mind:
	- That Hadoop is far more effective if you merge all the files you are using into one before running (you can do this with 'cat')
	- That you need to move the file(s) you want to run to HDFS
	- That you can obtain the running time in Linux using the 'time' command (> time hadoop ...)

- Change the WordCount program to do the following
	- Ignore punctuation marks
	- Eliminate HTML commands and url addresses
	- write a Hadoop (Streaming) program to:
		- Compute the average use of every word,
		- Compute the maximum and minimum times a word appears in all the addresses
	- Starting in 1984, compute the average and standard deviation of times a word appears in a window of five years
	- Use the previous result to output the words that appear in a given year with a frequency that exceeds the average plus two standard deviations