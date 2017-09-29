"""
Project Euler
Problem 47: Distinct primes factors

Answer: 134043
"""
import math

class DistinctPrimeFactors:
	def __isPrime(self, num):
		"""
		Checks primality by testing all possible divisors up to the square root
		of num.
		"""
		if num == 2 or num == 3:
			return True, None
		if num % 2 == 0 or num < 2:
			return False, 2

		for i in xrange(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False, i
		return True, None

	def __numDistinctFactors(self, num):
		"""
		Returns the number of distinct prime factors of num.
		"""
		distinctFactors = set()
		isPrime, factor = self.__isPrime(num)
		while not isPrime:
			distinctFactors.add(factor)
			num /= factor
			isPrime, factor = self.__isPrime(num)
		distinctFactors.add(num)
		return len(distinctFactors)

	def __isDone(self, nConsecutive, n):
		"""
		Returns True if all n numbers in nConsecutive have n distinct factors,
		and False otherwise.
		"""
		if len(nConsecutive) < n:
			return False

		for num, numDistinctFactors in nConsecutive:
			if numDistinctFactors < n:
				return False
		return True

	def firstNConsecutiveNPrimeFactors(self, n):
		"""
		Returns the smallest of the first n consecutive numbers to each have n 
		distinct prime factors.
		"""
		nConsecutive = []
		i = 2
		while not self.__isDone(nConsecutive, n):
			if len(nConsecutive) >= n:
				nConsecutive.pop(0)
			nConsecutive.append((i, self.__numDistinctFactors(i)))
			i += 1
		return nConsecutive[0][0]

print DistinctPrimeFactors().firstNConsecutiveNPrimeFactors(4)
