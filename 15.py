"""
Project Euler
Problem 15: Lattice paths

Answer: 137846528820
"""

def numLatticePaths(m, n):
	"""
	Number of lattice paths (Manhattan walks) from (0,0) to (m, n) is equivalent
	to picking the order of the m moves down and n moves right. Or in a boolean
	string of length m+n, choosing which m bits are 1 (the remaining n are set
	to 0) = (m+n m).
	"""
	ans = 1
	for i in xrange(m+n, m, -1):
		ans *= i
	for i in xrange(1, n + 1):
		ans /= i
	return ans

print numLatticePaths(20, 20)

