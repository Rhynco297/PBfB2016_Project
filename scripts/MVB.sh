#! /bin/zsh
#Execute using zshell
#Needs to be executed in directory of Hours.csv

#GOAL: extract names, numbers and worked hours from csv file

#Names always come in the line after one with "Medewerker:" in it.
#Step 1: grep line with "Medewerker:" plus one line below
#Step 2: pipeline it to a grep that looks for everything except "Medewerker:".
#Step 3: pipeline it to a grep that looks for everything except "--" at the beginning of the line
#Step 4: redirect to file
grep -A1 'Medewerker:' Hours.csv | grep -v 'Medewerker:' | grep -v '^--' > Names.txt

#The header (which shows the order of datapoints) always has "Projectnr." in it
#Step 1: grep line with "Projectnr." in it
#Step 2: pipeline to keeping only the last line
#Step 3: redirect to file to create the header
grep "Projectnr." Hours.csv | tail -n 1 > Work.txt

#Hour data always comes in a line with a U followed by 9 digits (e.g. U101400002)
#Step 1: grep line with "U[0-9]\{\9}" in it
#Step 2: 'Feestdagen' is non-useful info which can cause trouble later on, so grep to look for all except 'Feestdagen'
#Step 2: append to work file
grep "U[0-9]\{9\}" Hours.csv | grep -v 'Feestdagen' >> Work.txt

Reorganize.py #Continue to execute python script


