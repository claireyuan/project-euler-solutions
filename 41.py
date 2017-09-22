"""
Project Euler
Problem 41: Pandigital prime

Answer: 7652413
"""
import math

def isPandigital(num):
	"""
	Returns True if the given n-digit number contains each digit from 1 to n 
	exactly once.
	"""
	numAsString = sorted(str(num))
	allDigits = map(str, range(1, len(numAsString) + 1))
	return len(numAsString) < 10 and numAsString == allDigits

def isPrime(num):
	"""
	Returns True if num is prime, and False otherwise.
	"""
	if num < 2:
		return False
	if num == 2:
		return True

	for i in xrange(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def largestNDigitPandigitalPrime(n):
	"""
	Returns the largest n-digit pandigitial prime.
	"""
	upperBound = 9
	for i in xrange(n - 1):
		upperBound = upperBound * 10 + 9
	lowerBound = upperBound / 10
	
	for i in xrange(upperBound, lowerBound, -1):
		if isPandigital(i) and isPrime(i):
			return i

def largestPandigitalPrime():
	"""
	Returns the largest pandigitial prime.
	"""
	# Pandigital numbers of length 8 and 9 must be divisible by 3
	for n in xrange(7, 0, -1):
		pandigitalPrime = largestNDigitPandigitalPrime(n)
		if pandigitalPrime is not None:
			return pandigitalPrime

print largestPandigitalPrime()