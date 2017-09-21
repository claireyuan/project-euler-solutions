"""
Project Euler
Problem 29: Distinct powers

Answer: 9183
"""

def countDistinctIntegerCombinations(A, B):
	"""
	Counts the distinct terms generated by a^b for 2 <= a <= A and 2 <= b <= B.
	"""
	distinct = set()
	for a in xrange(2, A + 1):
		for b in xrange(2, B + 1):
			distinct.add(a**b)
	return len(distinct)

print countDistinctIntegerCombinations(100, 100)