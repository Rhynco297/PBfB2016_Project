#! /bin/zsh

#To calculate how many hours were worked in a week, we need to grep the right weeks
#Step 1: Let user decide which week to calculate
#Step 2: Grep the right weeks
#Step 3: Redirect to a file
#Step 4: Continue with a python script that processes the new file

echo "For which week would you like to calculate worked hours? (yyyyww, e.g. 201549) "
read WEEK			   #Save the week number as variable

grep $WEEK ./Re_Hours.csv > $WEEK.csv

echo "File $WEEK.csv created"

#calc.py
