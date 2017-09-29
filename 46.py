"""
Project Euler
Problem 46: Goldbach's other conjecture

Answer: 5777
"""
import math

def isPrime(num):
	"""
	Checks primality by testing all possible divisors up to the square root
	of num.
	"""
	if num <= 2:
		return num == 2

	for i in xrange(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def followsConjecture(num):
	"""
	Returns True if num can be written as the sum of a prime and twice a square.
	False otherwise.
	"""
	for i in xrange(1, int(math.sqrt(num)) + 1):
		if isPrime(num - (2 * i * i)):
			return True
	return False

def smallestConjectureException():
	"""
	Returns the smallest odd composite that cannot be written as the sum of a 
	prime and twice a square.
	"""
	i = 9
	while isPrime(i) or followsConjecture(i):
		i += 2
	return i

print smallestConjectureException()

