"""
Project Euler
Problem 22: Names scores

Answer: 871198282
"""

def readFile(fileName):
	"""
	Reads the comma separated text file of names and sorts them alphabetically.
	Returns the alphabetized names as a list of strings.
	"""
	f = open(fileName, 'r')
	names = map(lambda s: s[1:-1], f.read().split(','))
	names.sort()
	return names

def calculateValue(name):
	"""
	Calculates the alphabetical value of name.
	"""
	score = 0
	for c in name:
		score += ord(c) - ord('A') + 1
	return score

def sumNameScores(fileName):
	"""
	Sums the name scores of all names in fileName.
	"""
	names = readFile(fileName)
	summ = 0
	for i, name in enumerate(names):
		summ += (i + 1) * calculateValue(name)
	return summ

print sumNameScores('22names.txt')