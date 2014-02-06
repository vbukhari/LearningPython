#@author: Vasim Bukhari
# Homework 2 Advance Python 
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k','l','m','n','p','q','r','s','t','v','w','x','z','y'}

text = raw_input("Please Enter Text Here: ").lower();
NumVowels = NumConsonants = NumWorlds = 0 

for x in vowels: NumVowels = NumVowels + text.count(x)
print "Number of Vowels in Text: %d" % NumVowels

for x in consonants: NumConsonants = NumConsonants + text.count(x)
print "Number of Consonants in Text: %d" % NumConsonants

print "Number of Total Worlds in Text: %d" % len(text.split(" "))
