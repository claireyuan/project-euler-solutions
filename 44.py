"""
Project Euler
Problem 44: Pentagon numbers

Answer: 5482660
"""
import math

class PentagonNumbers:
	def __init__(self):
		self.pentagonalNumbers = [1]
		self.n = 2

	def __isPentagonal(self, number):
		"""
		Returns True is number is pentagonal, False otherwise, and stores the 
		pentagonal numbers up to number.
		"""
		while number > self.pentagonalNumbers[-1]:
			self.pentagonalNumbers.append(self.n * (3 * self.n - 1) / 2)
			self.n += 1
		return number in self.pentagonalNumbers

	def __getNthPentagonalNumber(self, n):
		"""
		Gets the nth pentagonal number and stores all pentagonal numbers up to
		it.
		"""
		while len(self.pentagonalNumbers) <= n:
			self.pentagonalNumbers.append(self.n * (3 * self.n - 1) / 2)
			self.n += 1
		return self.pentagonalNumbers[n - 1]

	def minimizeD(self):
		"""
		Minimizes the difference between pairs of pentagonal numbers where both 
		their sum and difference are also pentagonal.
		"""
		d = None
		for i in xrange(1, 10000):
			p_sum = self.__getNthPentagonalNumber(i)
			for j in xrange(1, i if d is None else min(d, i)):
				p_j = self.__getNthPentagonalNumber(j)
				p_k = p_sum - p_j
				p_diff = abs(p_k - p_j)
				if self.__isPentagonal(p_k) and self.__isPentagonal(p_diff):
					print p_j, p_k, p_diff
					d = p_diff if d is None else min(d, p_diff)
		return d

print PentagonNumbers().minimizeD()