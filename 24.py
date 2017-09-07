"""
Project Euler
Problem 24: Lexicographic permutations

Answer: 2783915460
"""

class LexicographicPermutations:
	def __init__(self, digits):
		"""
		Initialize with the digits we intend to use. Configurable mainly for 
		testing.
		"""
		self.permutations = []
		self.digits = digits
		self.n = 0

	def __generateDigitLexicographicPermutations(self, cur):
		"""
		Recursively generates lexicographic permutations and stores them in the
		self.permutations field once a complete permutation is generated. 
		Returns the self.nth permutations.
		"""
		if len(cur) == len(self.digits):
			self.permutations.append(cur)
			if len(self.permutations) == self.n:
				return cur
		for digit in self.digits:
			if digit not in cur:
				res = self.__generateDigitLexicographicPermutations(cur + digit)
				if res is not None:
					return res

	def getNthLexicographicPermutation(self, n):
		"""
		Wrapper to define self.n and to start the recursive function.
		"""
		self.n = n
		return self.__generateDigitLexicographicPermutations('')

digitPermutations =  LexicographicPermutations('0123456789')
print digitPermutations.getNthLexicographicPermutation(1000000)