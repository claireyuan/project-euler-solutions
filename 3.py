"""
Project Euler
Problem 3: Largest prime factor

Answer: 6857
"""
import math
import random

class PrimeNumberGenerator:
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
		for i in xrange(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
		return True

	def isPrimeUsingPrevPrimes(self, num):
		for prime in self.prev:
			if num % prime == 0:
				return False
		return True

	def nextPrime(self):
		num = self.cur + 1
		while not self.isPrime(num):
			num += 1
		self.cur = num
		self.prev.append(num)
		# print num
		return num

def primeFactors(num):
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

print primeFactors(600851475143)

