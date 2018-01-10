"""
Project Euler
Problem 52: Permuted multiples

Answer: 142857
"""

class PermutedMultiples:
	def __isPermutation(self, x, y):
		"""
		Returns True iff the digits of x are a permutation of the digits of y.
		"""
		xDigits = sorted(str(x))
		yDigits = sorted(str(y))
		return xDigits == yDigits

	def __isSolution(self, x):
		"""
		Returns True iff 2x, 3x, 4x, 5x, and 6x are all permutations of each 
		other.
		"""
		double = 2*x
		multiplier = 3
		while multiplier <= 6:
			if self.__isPermutation(double, multiplier * x):
				multiplier += 1
				continue
			return False
		return True

	def solve(self):
		"""
		Returns the smallest positive integer x such that 2x, 3x, 4x, 5x, and 6x
		are permutations of each other and the multiples that fulfill this 
		property.
		"""
		i = 1
		while True:
			if self.__isSolution(i):
				return i, map(lambda m: m*i, range(2, 7))
			i += 1

print PermutedMultiples().solve()