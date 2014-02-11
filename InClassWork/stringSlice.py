#!/usr/bin/env python

def is_palidromeSlice(s):
	return s == s[::-1]

print is_palidromeSlice("abcba")
print is_palidromeSlice("steven")
print is_palidromeSlice("banana")
