#! /usr/bin/python
import re #Allow use of regular expressions

#Define formula for creating a random string of letters as Surname
import string
import random
def Name_gen(size=8, chars=string.ascii_uppercase + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

#Define formula for creating random string of digits as Number
import string
import random
def No_gen(size=6, chars=string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

Names = open("Names.txt", "r") #Open original file to read from
Names2 = open("Names2.txt", "a") #Create new file to append to

Employees = {}	#Create empty dictionary for Employees
for Line in Names:
	#Define search string:
	SearchStr = '^(\d+)\t([^\s]+)\s([^\t]+)\t([^\t]+).+$' #Capture the personal number, first name and last name
	#Implement search string in search command:
	Result = re.search(SearchStr, Line) #Apply search command to CSV
	#Save captured items in new variables:
	Number = str(Result.group(1)) #Save as string, because personal number is NOT for calculations
	Surname = str(Result.group(2))
	Initials = str(Result.group(3))
	Other = str(Result.group(4))
	#Remove spaces from Initials
	Initials = Initials.strip()
	Cognito = str(Name_gen) + ", " + Initials #Save fake last name with real initials
	FakeNo = str(No_gen)
	Employees[Number] = [FakeNo] #Save fake number in dictionary, with real number as key
	Names2.write('%s\t%s\t%s' % (FakeNo, Cognito, Other)) #Append to Names2.txt and create incognito file

print "New file Names2.txt created..."

#Close files
Names.close()
Names2.close()

Work = open("Work.txt", "r") #Open original file to read from
Work2 = open("Work2.txt","a") #Create new file to append to

count = 0 #Set a counter and set it to zero

#Write header
Work2.write('Personal Number\tProjectnr.\tOmschrijving\tWeek\tJob\t0\tNormale uren\tO1\tO2\tT1\tT2\tT3\tUren VI\tUren VII\tDagen\tSvw-dag')

for Line in Work:
	if count > 0: #Skip the header
		SearchStr = '^(\d+)\t(.+)$' #Finds each full line once and captures number, plus everything else in one
		Result = re.search(SearchStr, Line)
		Number2 = str(Result.group(1))
		Other = str(Result.group(2))
		FakeNo = str(Employees[Number2])
		Work2.write('%s\t%s' % (FakeNo, Other)) #Append to Work2.txt and create incognito file
	count = count + 1

print "New file Work2.txt created..."

#Close files
Work.close()
Work2.close()

print "DONE"


