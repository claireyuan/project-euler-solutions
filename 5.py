"""
Project Euler
Problem 5: Smallest multiple

Answer: 232792560
"""

def smallestMultiple(upperBound):
	"""
	Returns the smallest positive number that is evenly divisible by all of the
	numbers from 1 to upperBound (inclusive). We do this by reducing common 
	factors between divisors in the range to produce the minimum list of 
	divisors with the same divisibility as the original range and multiplying
	them together. 
	"""
	divisors = range(1, upperBound + 1)
	for i, elem in enumerate(divisors):
		for j in xrange(i + 1, len(divisors)):
			if divisors[j] % elem == 0:
				divisors[j] /= elem
	return reduce(lambda x, y: x*y, divisors)

print smallestMultiple(20)
