"""
Project Euler
Problem 10: Summation of primes

Answer: 142913828922
"""

class PrimeNumberGenerator:
	"""
	Generates prime numbers. Initialize, then use nextPrime to get the next 
	prime in the sequence.
	"""
	def __init__(self, maxValue):
		self.prev = []
		self.cur = 1
		self.maxValue = maxValue

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

	def __iter__(self):
		return self

	def next(self):
		"""
		Generates the next largest prime number in the sequence and stores it 
		for future primality testing.
		"""
		num = self.cur + 1
		if num > self.maxValue:
			raise StopIteration
		while not self.isPrime(num):
			if num >= self.maxValue:
				raise StopIteration
			num += 1
		self.cur = num
		self.prev.append(num)
		return num

	def __next__(self):
		return self.next()

def sumPrimes(upperBound):
	return sum(PrimeNumberGenerator(upperBound))

print sumPrimes(2000000)

