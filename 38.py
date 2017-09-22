"""
Project Euler
Problem 38: Pandigital multiples

Answer: 932718654
"""

DIGITS = '123456789'
def isPandigital(numAsString):
	"""
	Returns True if numAsString contains all digits between 1 and 9, and False
	otherwise.
	"""
	return ''.join(sorted(numAsString)) == DIGITS

def getLargestPandigitalMultiple():
	"""
	Gets the largest 1 to 9 pandigital 9-digit number that can be formed as the 
	concatenated product of an integer x with (1, 2, ... , n) where n > 1. 
	Prunes the search space by only searching for integers x that are greater 
	than the first len(x) digits of the current largest pandigital product.
	"""
	num, largestPandigitalProduct = 1, '123456789'
	while len(str(num)) <= 5:
		concatProduct = str(num)
		multiplier = 1
		while len(concatProduct) < 9:
			multiplier += 1
			concatProduct += str(num * multiplier)
			
		if multiplier > 1 and isPandigital(concatProduct):
			largestPandigitalProduct = max(concatProduct, largestPandigitalProduct)
		
		num += 1
		if str(num) < largestPandigitalProduct[:len(str(num))]:
			num = int(largestPandigitalProduct[:len(str(num))])

	return largestPandigitalProduct

print getLargestPandigitalMultiple()