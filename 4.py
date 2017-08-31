"""
Project Euler
Problem 4: Largest palindrome product

Answer: 906609
"""

def isPalindrome(num):
	"""
	Returns true if the given number is a palindrome. 
	Requires that num is an int and num >= 0.
	"""
	num_string = str(num)
	for i in xrange(len(num_string)/2):
		if num_string[i] != num_string[len(num_string)-1-i]:
			return False
	return True 


def getLargestPalindrome(lowerBound, upperBound):
	"""
	Finds the largest palindrome made from the product of two numbers from 
	the range [lowerBound, upperBound).
	"""
	largestPalindrome = 0
	for i in xrange(lowerBound, upperBound):
		for j in xrange(i, upperBound):
			product = i * j
			if isPalindrome(product) and product > largestPalindrome:
				largestPalindrome = product
	return largestPalindrome
	
print getLargestPalindrome(100, 1000)