echo "Merge and Exceute Start"
echo "0% complete..."
#concat the files in folder to a single file. (25% data)
cat part1/* >>inputfile.txt
echo "merge complete..."
sleep 5
#create the directory
#hadoop fs -mkdir /user/jmistry2/input/
#move file to HDFS
hadoop fs -put inputfile.txt /user/jmistry2/input/
echo "moving complete..."
sleep 5s
#execute hadoop and obtain running time using 'time' command and direct its output to 'runningtime.txt'
#'>>' is for appending the output to file
(time hadoop jar /apps/hadoop-2/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /user/jmistry2/input/ /user/jmistry2/output/) 2>> runningtime.txt
hadoop fs -rm -r /user/jmistry2/output/
hadoop fs -rm -r /user/jmistry2/input/inputfile.txt
echo "25% complete..."
#concat the files in folder to a single file. (50% data)
cat part2/* >>inputfile.txt
echo "merge complete..."
sleep 5s
#move file to HDFS
hadoop fs -put inputfile.txt /user/jmistry2/input/
echo "moving complete..."
sleep 5s
#execute hadoop and obtain running time using 'time' command and direct its output to 'runningtime.txt'
#'>>' is for appending the output to file
(time hadoop jar /apps/hadoop-2/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /user/jmistry2/input/ /user/jmistry2/output/) 2>> runningtime.txt
#remove the files from HDFS
hadoop fs -rm -r /user/jmistry2/output/
hadoop fs -rm -r /user/jmistry2/input/inputfile.txt
echo "50% complete..."
#concat the files in folder to a single file.(75% data)
cat part3/* >>inputfile.txt
echo "merge complete..."
sleep 5s
#move file to HDFS
hadoop fs -put inputfile.txt /user/jmistry2/input/
echo "moving complete..."
sleep 5s
#execute hadoop and obtain running time using 'time' command and direct its output to 'runningtime.txt'
#'>>' is for appending the output to file
(time hadoop jar /apps/hadoop-2/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /user/jmistry2/input/ /user/jmistry2/output/) 2>> runningtime.txt
#remove the files from HDFS
hadoop fs -rm -r /user/jmistry2/output/
hadoop fs -rm -r /user/jmistry2/input/inputfile.txt
echo "75% complete..."
#concat the files in folder to a single file.(100% data)
cat part4/* >>inputfile.txt
echo "merge complete..."
sleep 5s
#move file to HDFS
hadoop fs -put inputfile.txt /user/jmistry2/input/
echo "moving complete..."
sleep 5s
#execute hadoop and obtain running time using 'time' command and direct its output to 'runningtime.txt'
#'>>' is for appending the output to file
(time hadoop jar /apps/hadoop-2/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /user/jmistry2/input/ /user/jmistry2/output/) 2>> runningtime.txt
#remove the files from HDFS
hadoop fs -rm -r /user/jmistry2/output/
hadoop fs -rm -r /user/jmistry2/input/inputfile.txt
echo "100% complete..."
echo "Merge and Execute End"