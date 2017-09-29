"""
Project Euler
Problem 45: Triangular, pentagonal, and hexagonal

Answer: 1533776805
"""

def getTriangleNum(n):
	"""
	Returns the nth triangle number.
	"""
	return n * (n + 1) / 2

def getPentagonalNum(n):
	"""
	Returns the nth pentagonal number.
	"""
	return n * (3 * n - 1) / 2

def getHexagonalNum(n):
	"""
	Returns the nth hexagonal number.
	"""
	return n * (2 * n - 1)

def triangularPentagonalHexagonal(startIndex_t=0, startIndex_p=0, startIndex_h=0):
	"""
	Returns the first triangle number after startIndex_t that is also pentagonal 
	and hexagonal. Default is to start from n = 1.
	"""
	index_t = startIndex_t + 1
	index_p = startIndex_p + 1
	index_h = startIndex_h + 1
	t = getTriangleNum(index_t)
	p = getPentagonalNum(index_p)
	h = getHexagonalNum(index_h)
	while t != getPentagonalNum(index_p) or t != getHexagonalNum(index_h):
		index_t += 1
		t = getTriangleNum(index_t)
		if t > p:
			index_p += 1
			p = getPentagonalNum(index_p)
		if t > h:
			index_h += 1
			h = getHexagonalNum(index_h)
	return t

print triangularPentagonalHexagonal(285, 165, 143)