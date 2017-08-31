"""
Project Euler
Problem 6: Sum square difference

Answer: 25164150
"""

def sumSquareDifference(upperBound):
	"""
	Returns the difference between the sum of squares and the square of the sum 
	of the natural numbers up to upperBound (inclusive).
	"""
	sumOfSquares = reduce(lambda x, y: x + y*y, xrange(1, upperBound+1), 0)
	summ = sum(xrange(1, upperBound+1))
	squareOfSum = summ * summ

	return squareOfSum - sumOfSquares

print sumSquareDifference(100) 