"""
Project Euler
Problem 37: Truncatable primes

Answer: 748317
"""

class TruncatablePrimes:
	def __init__(self):
		self.leftTruncatablePrimes = []
		self.rightTruncatablePrimes = []
		self.primes = [2, 3, 5, 7]

	def __isPrime(self, num):
		if num < 2:
			return False

		if num in self.primes:
			return True

		for prime in self.primes:
			if num % prime == 0:
				return False
		self.primes.append(num)
		return True

	def __isLeftTruncatablePrime(self, numAsString):
		"""
		Returns True if input is prime and repeatedly removing the leftmost 
		digit maintains the primality of the number. Takes the number as a 
		string in decimal format.
		"""
		if len(numAsString) == 0 or numAsString in self.leftTruncatablePrimes:
			return True
		if self.__isPrime(int(numAsString)) \
			and self.__isLeftTruncatablePrime(numAsString[1:]):
			self.leftTruncatablePrimes.append(numAsString)
			return True
		return False

	def __isRightTruncatablePrime(self, num):
		"""
		Returns True if input is prime and repeatedly removing the rightmost 
		digit maintains the primality of the number. Takes the number as an int.
		"""
		if num == 0 or num in self.rightTruncatablePrimes:
			return True
		if self.__isPrime(num) \
			and self.__isRightTruncatablePrime(num / 10):
			self.rightTruncatablePrimes.append(num)
			return True
		return False

	def getTruncatablePrimes(self):
		"""
		Returns all eleven primes that are both truncatable from left to right 
		and right to left.
		"""
		truncatablePrimes = []
		i = 11
		while len(truncatablePrimes) < 11:
			if self.__isRightTruncatablePrime(i) and self.__isLeftTruncatablePrime(str(i)):
				truncatablePrimes.append(i)
			i += 1
		return truncatablePrimes

print sum(TruncatablePrimes().getTruncatablePrimes())

