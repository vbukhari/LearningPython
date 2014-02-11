#Vasim Bukhari
#Homework 2 Advance Python 
#This program take input a list of names in "Last Name, First Name," i.e., last name, comma, first name.
#when/if the user types the names in the wrong order, i.e., "First Name Last Name," the error is corrected,
# and the user is notified.
#also keep track of the number of input mistakes.
#When the user is done,it sort the list, and display the sorted names in "Last Name, First Name" order.
from operator import itemgetter

inputMistakes = 0
Names = []
NumNames = int(raw_input("How many names you want to enter?: "))

for x in range(NumNames):
	inputName = raw_input("Please Enter Name %d: " % x)
	if inputName.count(','):
		name = inputName.split(', ')
		# Names.reverse()
	else:
		inputMistakes += 1
		name = inputName.split(' ')
		name.reverse()
		print "Name is in wrong order(Correct Order: Last Name, First Name): order corrected!"
		print "Please check your input format, Number of Mistakes done %d times" % inputMistakes
	
	Names.append(name)

print "The sorted List Names in order: Last Name, First Name:"
for x in sorted(Names, key=itemgetter(0)):
	print x[0], ', ', x[1]