#!/usr/bin/env python
import os

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter filename: ')
print

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
