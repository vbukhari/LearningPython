#!/usr/bin/env python

'readNwriteTextFile.py create text file or read and display text file'

import os

str = raw_input("Enter '1' to create new file.\nEnter '2' to display exists file. \n>>>>> ")

if str == '1':
	#while True:
	#ls = os.linesep
	# get filename
	while True:
		fname = raw_input('Enter file name: ')
		if os.path.exists(fname):
	#try:
		#os.path.exists(fname)
	#except IOError, e:
			print "ERROR: '%s' already exists, choose different name! " % fname#, e
		else:
			break
	
	# get file content (text) lines
	all = []
	print "\nEnter lines ('.' by itself to quit).\n"
	#loop until user terminates input
	while True:
		entry = raw_input('> ')
		if entry == '.':
			break
		else:
			all.append(entry)
	# write lines to file with proper line-ending
	fobj = open(fname, 'w')
	fobj.write('\n'.join(all))
	fobj.close()
	print 'DONE!'

elif str == '2':
	'readTextFile.py -- read and display text file'

	# get filename
	fname = raw_input('Enter filename: ')
	
	# attempt to open file for reading
	try:
		os.path.exists(fname)
		fobj = open(fname, 'r')
	except IOError, e:
	    #print "*** file open error: ", e
	    print "ERROR: '%s' doesn't exists: " % fname, e
	else:
	# display contents to the screen
	    for eachLine in fobj:
	    	eachLine = eachLine.strip()
	        print eachLine
	    fobj.close()
		
else:
	print "ERROR: Invalid input.."