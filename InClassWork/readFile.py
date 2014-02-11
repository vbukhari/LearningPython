
textFile = open('data.txt', 'r')
wordList = [line.split() for line in textFile]
#L = textFile.read().split('\n'))
for i in range(len(k)):
	if len(k[i])==4:
		k[i] = '****'