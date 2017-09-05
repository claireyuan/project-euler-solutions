"""
Project Euler
Problem 14: Longest Collatz sequence

Answer: 837799
"""

class LongestCollatzSequence:
	def __init__(self):
		self.collatzSequenceLengthMap = {1:1}

	def __getChainLength(self, number):
		"""
		Dynamic programming approach to finding the chain length. Calculate and 
		store the length of the chain starting at each intermediate value along 
		the chain until we can look up the length of the chain starting at the
		next value in the chain.
		"""
		if number in self.collatzSequenceLengthMap:
			return self.collatzSequenceLengthMap[number]
		if number % 2 == 0:
			length = 1 + self.__getChainLength(number / 2)
		else:
			length = 1 + self.__getChainLength(3 * number + 1)
		self.collatzSequenceLengthMap[number] = length
		return length

	def getLongestChainStart(self, upperBound):
		longestChainStart = (0, 0)
		for i in xrange(1, upperBound):
			longestChainStart = max(longestChainStart, (self.__getChainLength(i), i))
		length, startNum = longestChainStart
		return startNum

l = LongestCollatzSequence()
print l.getLongestChainStart(1000000)