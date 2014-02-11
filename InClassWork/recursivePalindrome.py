#!/usr/bin/env python
import os
import math
import string


def is_palindrome(s):	
	# if s == '':
	# 	return True
	# else:
	# 	if (ord(s[0])-ord(s[len(s)-1])) == 0:
	# 		return is_palindrome(s[1:len(s)-1])
	# 	else:
	# 		return False
	if s == '':
		return True
	else:
		if s[0] == s[-1]:
			return is_palindrome(s[1:-1])
		else:
			return False

print is_palindrome('aabbaa')
