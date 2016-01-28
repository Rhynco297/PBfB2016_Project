#! /usr/bin/python
#Needs to be executed in directory of Names.txt
import re #Allow the use of regular expressions

#Create a new file to write reorganized data to:
f = open('/home/manager/Documents/PBfB/Project/Encryption/Re_Hours.csv', 'w')
	#The 'w' is important here; if there was already some text there, it will be overwritten to 'clear' the file
f.write ('Number\tSurname, Initials\tWeek\tJob\thTotal\thNormal\n') #Create a header
f.close()	#Close the file again for now

#Open the Names file
Names = open("Names.txt", 'r')

#Put employee numbers & names in a dictionary
Employees = {}	#Create empty dictionary for Employees
for Line in Names:
	#print Line #Print to check what regular expression is needed while writing script
	#Define search string:
	SearchStr = '^(\d+)\t([^\s]+)\s([^\t]+).+$' #Capture the personal number, first name and last name
	#Implement search string in search command:
	Result = re.search(SearchStr, Line) #Apply search command to CSV
	#Save captured items in new variables:
	Number = str(Result.group(1)) #Save as string, because personal number is NOT for calculations
	Surname = str(Result.group(2))
	Initials = str(Result.group(3))
	#Remove spaces from Initials
	Initials = Initials.strip()
	Name = Surname + ", " + Initials #Save names in a nice format (e.g. 'Surname, I.N.')
	Employees[Number] = [Name] #Save name to number in dictionary

#print Employees #Print to check functionality while writing script
print "Recorded..... Employee Numbers, Names" #Give some feedback to know that this part did its job

#Close the Names file
Names.close()

#Open the Work file
Work = open("Work.txt", 'r')

#Add worked hours to the right numbers in the same dictionary
WorkWeeks = {}	#Create empty dictionary for workweeks
LineNo = 0 	#Start a line counter to exclude header from following search
f = open('/home/manager/Documents/PBfB/Project/Encryption/Re_Hours.csv', 'a') #Open the file with header to APPEND to
for Line in Work:
	if LineNo > 0:	#LineNumber 0 (which is the header) is not included in the search
		#print Line #Print to check what regular expression is needed while writing script
		SearchStr = '^(\d+).*(201\d{3,})\t([^\t]*)\t([^\t]*)\t([^\t]*).+$' #Checked in gEdit!
		Result = re.search(SearchStr, Line)
		Number2 = str(Result.group(1))	#Personal number of employee
		Week = str(Result.group(2))	#Week worked, is a string!
		Job = str(Result.group(3))	#Job number, also a string!
		hTotal = float(Result.group(4))	#Total hours worked, is a float to allow calculations
		hNormal = float(Result.group(5))	#Normal hours worked (excluding overtime etc.), is a float to allow calc
		Name = str(Employees[Number2])
		Name = Name.translate(None, "[']") #Take out the brackets and '' which are around the Names
		#print Number2, Name, Week, Job, hTotal, hNormal #While scripting, check if all variables are good
		f.write('%s\t%s\t%s\t%s\t%f\t%f\n' % (Number2, Name, Week, Job, hTotal, hNormal))
	LineNo = LineNo + 1	#Add 1 to linenumber

#Close the Work file
Work.close()

print 'New file created: Re_Hours.csv'

