"""
Project Euler
Problem 3: Largest prime factor

Answer: 6857
"""
import math
import random

class PrimeNumberGenerator:
	"""
	Generates prime numbers. Initialize, then use nextPrime to get the next 
	prime in the sequence.
	"""
	def __init__(self):
		self.prev = []
		self.cur = -1

	def isPrime(self, num):
		if num == 2 or num == 3:
			return True
		if num % 2 == 0 or num < 2:
			return False

		return self.isPrimeUsingPrevPrimes(num)

	def isPrimeNaive(self, num):
		"""
		Checks primality by testing all possible divisors up to the square root
		of num.
		"""
		for i in xrange(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
		return True

	def isPrimeUsingPrevPrimes(self, num):
		"""
		Checks primality by testing only the previously generated primes as 
		potential divisors.
		"""
		for prime in self.prev:
			if num % prime == 0:
				return False
		return True

	def nextPrime(self):
		"""
		Generates the next largest prime number in the sequence and stores it 
		for future primality testing.
		"""
		num = self.cur + 1
		while not self.isPrime(num):
			num += 1
		self.cur = num
		self.prev.append(num)
		# print num
		return num

def getLargestPrimeFactor(num):
	"""
	Returns the largest prime factor of num. 
	Requires that num is an int and num > 1
	"""
	largestPrimeFactor = None
	primeNumberGenerator = PrimeNumberGenerator()
	prime = primeNumberGenerator.nextPrime()
	while prime <= int(math.sqrt(num)) + 1:
		if num % prime == 0:
			largestPrimeFactor = prime
		prime = primeNumberGenerator.nextPrime()
	if largestPrimeFactor is None:
		return num
	return largestPrimeFactor

print getLargestPrimeFactor(600851475143)

