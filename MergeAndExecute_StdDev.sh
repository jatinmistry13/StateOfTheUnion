echo "Modified Merge and Exceute Start"
#concat the files in folder to a single file. (25% data)

#for filename in part1/*
#do
	#echo $filename
#	python fileToString.py $filename >>inputfile.txt
#done

for year in `seq 1984 1988`;
do
    python fileToString.py Strippedfiles/${year}* >> input-stddev.txt
done

echo "merge complete..."
sleep 5s
#move file to HDFS
hadoop fs -put input-stddev.txt /user/jmistry2/input/
echo "moving complete..."
sleep 5s
#execute hadoop and obtain running time using 'time' command and direct its output to 'runningtime.txt'
#'>>' is for appending the output to file
#(time hadoop jar /apps/hadoop-2/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /user/jmistry2/input/ /user/jmistry2/output/) 2>> runningtime.txt
#execute hadoop
hadoop jar /apps/hadoop-2/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar -input /user/jmistry2/input/ -output /user/jmistry2/output/ -mapper /home/jmistry2/wordCountMapper_StdDev.py -reducer /home/jmistry2/wordCountReducer_StdDev.py
#remove the files from HDFS
#hadoop fs -rm -r /user/jmistry2/output/
hadoop fs -get /user/jmistry2/output/* /home/jmistry2/StdDevOutput/

#hadoop fs -get output/part-00000 year-output
#cat year-output >> yearly
#rm year-output

hadoop fs -rm -r /user/jmistry2/input/inputfile.txt
echo "100% complete..."
echo "Modified Merge and Execute End"
