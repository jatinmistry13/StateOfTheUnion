#!/bin/bash

nSlideWinMin=1
nSlideWinMax=6
nStartYear=1984
nEndYear=1989
while [ $nSlideWinMax -le 33 ]
do
	echo "----$nStartYear - $nEndYear window----"
	sed -n "${nSlideWinMin},${nSlideWinMax}p" fullData.txt > inputfile.txt
    hadoop fs -put inputfile.txt /user/jmistry2/input/	
	echo "hadoop process starts"
	hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar -D mapred.map.tasks=1 -input /user/jmistry2/input/inputfile.txt -output /user/jmistry2/output -mapper /home/jmistry2/wordCountMapper_Sliding_StdDev.py -reducer /home/jmistry2/wordCountReducer_Sliding_StdDev.py
	hadoop fs -get /user/jmistry2/output/part-00000 /home/jmistry2/StdDevOutput/
	echo "hadoop process ends"
	mv /home/jmistry2/StdDevOutput/part-00000 /home/jmistry2/StdDevOutput/$nStartYear
	hadoop fs -rm -r /user/jmistry2/input/inputfile.txt 
	hadoop fs -rm -r /user/jmistry2/output/
	rm -r inputfile.txt
	#rm -r part-00000
	
	(( nSlideWinMin++ ))
	(( nSlideWinMax++ ))
	(( nStartYear++ ))
	(( nEndYear++ ))
	
done
