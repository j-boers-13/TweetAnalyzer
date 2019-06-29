#!/bin/sh
echo "This will extract the sample i chose from the data, filter the tweets on certain keywords, and then write the top keywords to tweetamounts.txt"

python3 createfiles.py

echo "Extracting tweets"
python3 dataExtraction.py

echo "Analyzing data"
python3 dataAnalysis.py
