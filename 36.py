"""
Project Euler
Problem 36: Double-base palindromes

Answer: 872187
"""

def isPalindrome(numAsStr):
	"""
	Given a string, returns True if it is a palindrome and False otherwise.
	"""
	for i in xrange(len(numAsStr) / 2):
		if numAsStr[i] != numAsStr[-i - 1]:
			return False
	return True

def isPalindromeBase10(num):
	"""
	Returns True if num is a palindrome in base 10, and False otherwise. 
	Requires that num is non-negative and does not allow leading zeros.
	"""
	return isPalindrome(str(num))

def isPalindromeBase2(num):
	"""
	Returns True if num is a palindrome in base 2, and False otherwise. 
	Requires that num is non-negative and does not allow leading zeros.
	"""
	return isPalindrome(str(bin(num))[2:])

def getDoubleBasePalindromes(upperBound):
	"""
	Returns all integers in the range [0, upperBound) that are palindromes in
	both base 10 and base 2.
	"""
	doubleBasePalindromes = []
	for i in xrange(upperBound):
		if isPalindromeBase10(i) and isPalindromeBase2(i):
			doubleBasePalindromes.append(i)
	return doubleBasePalindromes

print sum(getDoubleBasePalindromes(1000000))

