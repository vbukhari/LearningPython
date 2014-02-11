#!/usr/bin/env python

import math

def eval_loop():
	while True:
		input = raw_input('Enter Value Here:> ')
		if input == 'done':
			break
		else:
			result = eval(input)
		print result
	print result

eval_loop()