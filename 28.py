"""
Project Euler
Problem 28: Number spiral diagonals

Answer: 669171001
"""

def numberSpiralDiagonalSum(n):
	"""
	The sum of the numbers on the diagonals in a (n x n) spiral.
	"""
	summ = 1
	diff = 2
	curNum = 1
	for i in xrange(n / 2):
		for j in xrange(4):
			curNum += diff
			summ += curNum
		diff += 2
	return summ

print numberSpiralDiagonalSum(1001)