"""
Project Euler
Problem 23: Non-abundant sums

Answer: 4179871
"""
import math

class NonAbundantSums:
	def __init__(self):
		self.isAbundant = [False] * 11 + [None] * (28123 - 11)

	def __isAbundant(self, num):
		"""
		Returns true if num is an abundant number. Saves the result to avoid
		duplicate calculations.
		"""
		if self.isAbundant[num-1] is not None:
			return self.isAbundant[num-1]

		divisors = set([1])
		for i in xrange(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				divisors.add(i)
				divisors.add(num / i)
		self.isAbundant[num-1] = sum(divisors) > num
		return self.isAbundant[num-1]

	def __isSumOfTwoAbundantNums(self, num):
		"""
		Returns true if num is the sum of two abundant numbers and false 
		otherwise. 12 is the smallest abundant number.
		"""
		for a in xrange(12, num):
			if self.__isAbundant(a) and self.__isAbundant(num - a):
				return True
		return False

	def sumNonAbundantSums(self):
		"""
		Sums all of the positive integers which cannot be written as the sum of
		two abundant numbers. Because 12 is the smallest abundant number, all 
		positive integers < 24 cannot be written as the sum of two abundant 
		numbers. We are also given that all integers greater than 28123 can be
		written as the sum of two abundant numbers.
		"""
		summ = sum(xrange(1, 24))
		for i in xrange(24, 28123):
			if not self.__isSumOfTwoAbundantNums(i):
				summ += i
		return summ

print NonAbundantSums().sumNonAbundantSums()


