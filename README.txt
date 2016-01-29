----- NB: THIS ONLY WORKS FOR ORIGINAL FILE WHICH I DID NOT POST IN GITHUB, LOOK BELOW -----
>>> CREATING GRAPH <<<
Wil show normal worked hours and overtime per week

Step 1: Change working directory to folder with original csv file in it
Step 2: Execute MVB.sh -> This will automatically also run Reorganize.py and create a reorganized csv file
Step 3: Execute Graphs.R (By typing: RScript Graphs.R)
Step 4: The graph is automatically saved in the working directory

>> CALCULATING WEEK VALUES <<
Shows normal worked hours and overtime for specified week without creating a graph

Step 1: As above
Step 2: As above
Step 3: Execute week.sh
Step 4: Read values from the screen



----- FOR RUNNING WITH GITHUB FILES -----
>>> CREATING A GRAPH <<<

Step 1: Change working directory to the 'files' folder
Step 2: Run: ../scripts/Reorganize.py
Step 3: Run: Rscript ../scripts/Graphs.R
Step 4: The garph is automatically saved in the working directory

>>> CALCULATING WEEK VALUES <<<

Step 1: As above
Step 2: As above
Step 3: Run: ../scripts/week.sh
Step 4: Type in the desired week and read values from the screen

>>> TESTING THE ENCRYPTION SCRIPT <<

Step 1: Change working directory to the 'Encrypt example' folder
Step 2: Run: ../scripts/Encrypt.sh
Step 3: You are now left with an encrypted version of Name.txt and Work.txt (you can recognize them by the 2 in the name)
