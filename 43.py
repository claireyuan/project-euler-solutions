"""
Project Euler
Problem 43: Sub-string divisibility

Answer: 16695334890
"""

class SubstringDivisibility:
	def __init__(self):
		self.ans = set()
		self.divisible = [2, 3, 5, 7, 11, 13, 17]

	def __getSubstringDivisblePandigitals(self, curNum, allDigits):
		"""
		Builds (allDigits) pandigital numbers that satisfy the substring 
		divisibility property defined by self.divisible. Prunes the search space
		by only building up numbers where only the substrings that fulfil the 
		divisibility property will be added to.
		""" 
		if len(curNum) > 3:
			n = len(curNum) - 3
			if int(curNum[n:n+3]) % self.divisible[n-1] != 0:
				return

		if len(curNum) == 10:
			self.ans.add(curNum)
			return

		for digit in allDigits:
			if digit not in curNum:
				self.__getSubstringDivisblePandigitals(curNum + digit, allDigits)

	def solveProblem43(self):
		"""
		Finds the sum of all 0 to 9 pandigital numbers with the given property
		of substring divisibility.
		"""
		self.__getSubstringDivisblePandigitals('', '0123456789')
		return sum(map(int, self.ans))

print SubstringDivisibility().solveProblem43()
