#!/bin/sh
COMMAND=$1
OUTPUT_FILE=$2

if ! [ $# -eq 1 ]
  then
    echo "You must supply two arguments"
    exit 1
fi
START_TIME=$(date +%s%N)
eval $1
STOP_TIME=$(date +%s%N)

echo $START_TIME
echo $STOP_TIME
exit 0