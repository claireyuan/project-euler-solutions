"""
Project Euler
Problem 40: Champernowne's constant

Answer: 210
"""

class ChampernownesConstant:
	def __init__(self):
		self.constant = []
		self.curInt = 1

	def getNthDigit(self, n):
		"""
		Returns the nth digit of the fractional part of Champernowne's constant,
		created by concatenating the positive integers.
		"""
		while len(self.constant) <= n:
			i = str(self.curInt)
			for d in i:
				self.constant.append(d)
			self.curInt += 1
		return int(self.constant[n - 1])

	def solveProblem40(self):
		"""
		If dn represents the nth digit of the fractional part, returns the value
		of d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000.
		"""
		n = 1
		ans = 1
		for exp in xrange(7):
			ans *= self.getNthDigit(n)
			n *= 10
		return ans

print ChampernownesConstant().solveProblem40()
