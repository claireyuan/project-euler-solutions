"""
Project Euler
Problem 7: 10,001st prime

Answer: 104743
"""
import itertools

def filterPrime(iterable, prime):
	for x in iterable:
		if x % prime != 0:
			yield x

def generatePrimesSieve(count):
	""" 
	Generates a sequence of prime numbers by using a lazy programming sieve
	method. Exceeds the maximum recursion depth at large counts.
	"""
	if count < 1:
		return None

	sieve = itertools.count(3, 2)
	lastPrime = 2
	for i in xrange(1, count):
		lastPrime = sieve.next()
		print lastPrime
		sieve = filterPrime(sieve, lastPrime)
	return lastPrime

class PrimeNumberGenerator:
	"""
	Generates prime numbers. Initialize, then use nextPrime to get the next 
	prime in the sequence.
	"""
	def __init__(self):
		self.prev = []
		self.cur = -1

	def isPrime(self, num):
		"""
		Checks primality by testing only the previously generated primes as 
		potential divisors.
		"""
		if num == 2 or num == 3:
			return True
		if num % 2 == 0 or num < 2:
			return False

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

def generatePrimes(count):
	primeNumberGenerator = PrimeNumberGenerator()
	lastPrime = 0
	for i in xrange(count):
		lastPrime = primeNumberGenerator.nextPrime()
	return lastPrime

print generatePrimes(10001)

