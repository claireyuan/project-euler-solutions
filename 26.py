"""
Project Euler
Problem 26: Reciprocal cycles

Answer: 983
"""

def generateDecimal(d):
	"""
	Generates the decimal representation of 1/d two digits at a time.
	"""
	divisor = 10
	while True:
		digit1 = divisor / d
		divisor = (divisor % d) * 10
		digit2 = divisor / d
		divisor = (divisor % d) * 10
		yield digit1, digit2
		

class LongestRecurringCycle:
	def __init__(self, upperBound):
		self.cycleLengths = [None] * upperBound

	def __hasRecurringCycle(self, d):
		"""
		Returns True if 1/d has a recurring cycle, False if it is a finite 
		decimal.
		"""
		if d == 1 or d == 2 or d == 5:
			return False, None
		if d % 2 == 0:
			return self.__hasRecurringCycle(d / 2)
		if d % 5 == 0:
			return self.__hasRecurringCycle(d / 5)
		return True, d

	def __lengthRecurringCycle(self, d):
		"""
		Calculates the length of the recurring cycle in the decimal 
		representation of 1/d. Requires that 1/d contains a recurring cycle and 
		d is a postitive integer. Relies on the fact that the longest recurring
		cycle can be at most d-1 in length.
		"""
		if d - 1 < len(self.cycleLengths) and self.cycleLengths[d - 1] is not None:
			return self.cycleLengths[d - 1]

		decimal = []
		decimalGenerator = generateDecimal(d)
		longest = []
		while len(decimal) < 2 * (d - 1):
			digit1, digit2 = decimalGenerator.next()
			decimal.append(digit1)
			decimal.append(digit2)
			if decimal[:len(decimal)/2] == decimal[len(decimal)/2:] \
				and not self.__isMultiple(len(decimal)/2, longest):
				longest.append(len(decimal)/2)
		return max(longest)

	def __isMultiple(self, length, lengths):
		"""
		Returns True if length is an integer multiple of an element of lengths
		(not including 1), False otherwise.
		"""
		for l in lengths:
			if l != 1 and length % l == 0:
				return True
		return False

	def getLongestRecurringCycle(self, upperBound):
		"""
		Gets the d < upperBound for which 1/d contains the longest recurring 
		cycle in its decimal representation.
		"""
		for i in xrange(1, upperBound):
			hasRecurringCycle, repeating = self.__hasRecurringCycle(i)
			if hasRecurringCycle:
				self.cycleLengths[i - 1] = self.__lengthRecurringCycle(repeating)
			else:
				self.cycleLengths[i - 1] = 0
		return self.cycleLengths.index(max(self.cycleLengths[:upperBound])) + 1

print LongestRecurringCycle(1000).getLongestRecurringCycle(1000)

