import os
# dictionary = {}
# while True:
# 	inputName = raw_input("Enter Your Name: ")
# 	if not inputName: break
# 	inputFruit = raw_input("Enter Fruit Name: ")
# 	dictionary[inputName] = inputFruit
# print dictionary

#Tindell
dictionary = {}
while True:
	inputName = raw_input("Enter Name: ")
	if not inputName: break
	food = raw_input("Enter Food Name: ")
	if inputName in dictionary:
		dictionary[inputName].append(food)
	else:
		dictionary[inputName] =  [food]
for i in dictionary:
	print i, "likes", 
	if len(dictionary[i]) == 1:
		print dictionary[i][0]
	else:
		print ','.join(dictionary[i][:-1])+" and "+dictionary[i][-1]
#Jim

