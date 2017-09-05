"""
Project Euler
Problem 17: Number letter counts

Answer: 21124
"""

counts = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, \
		  11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, \
		  20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

def lettersToThousands(upperBound):
	"""
	Counts the letters used to write out all the numbers from [1, upperBound] in
	words.
	"""
	totalNumLetters = 0
	for i in xrange(1, upperBound + 1):
		thousands = i / 1000
		hundreds = (i / 100) % 10
		tens = (i / 10) % 10
		digit = i % 10

		numLetters = 0
		if thousands > 0:
			numLetters += counts[thousands] + len('thousand')
		if hundreds > 0:
			numLetters += counts[hundreds] + len('hundred')
		if (thousands > 0 or hundreds > 0) and (tens > 0 or digit > 0):
			numLetters += len('and')
		if tens == 1:
			numLetters += counts[i % 100]
		elif digit > 0:
			numLetters += counts[digit]
		if tens > 1:
			numLetters += counts[tens * 10]
		totalNumLetters += numLetters
	return totalNumLetters

print lettersToThousands(1000)
