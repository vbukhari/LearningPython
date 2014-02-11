from operator import itemgetter

totalWrongInput = 0
def validateUserInput(userInput):
	global totalWrongInput
	if userInput.count(','):
		listName = userInput.split(', ')
	else:
		totalWrongInput += 1
		listName = userInput.split(' ')
		listName.reverse()
		print ">> Wrong format... should be Last, First."
		print ">> You have done this %d time(s) already. Fixing input..." % totalWrongInput
	return listName

listName = []
totalNumName = int(raw_input('Enter total number of names: '))

for i in range(totalNumName):
	userInput = raw_input("Please enter name %d: " % i)
	newName = validateUserInput(userInput)
	listName.append(newName)

print 'The sorted list (by last name) is:'
for i in sorted(listName, key=itemgetter(0)):
	print i[0], ', ', i[1]