"""
Project Euler
Problem 18: Maxiumum path sum I

Answer: 1074
"""

class Triangle:
	"""
	Define a Triangle node to have a value, left child, right child, and max
	sum path with the current node as the root.
	"""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.maxPath = None

class TrianglePathSum:
	"""
	Dynamic programming approach to solving triangle path sum. At each node, 
	store the maximum path sum of the triangle with node as its root.
	"""
	def __init__(self, triangle):
		self.triangle = self.parseTriangle(triangle)

	def parseTriangle(self, triangleString):
		rows = triangleString.split('\n')
		elems = [[Triangle(int(n)) for n in row.split()] for row in rows]
		for r in xrange(len(elems) - 1):
			for i in xrange(len(elems[r])):
				elems[r][i].left = elems[r+1][i]
				elems[r][i].right = elems[r+1][i+1]
		return elems[0][0]

	def __getMaxPathSumHelper(self, node):
		if node.maxPath is not None:
			return node.maxPath
		leftMax = 0
		rightMax = 0
		if node.left is not None:
			leftMax = self.__getMaxPathSumHelper(node.left)
		if node.right is not None: 
			rightMax = self.__getMaxPathSumHelper(node.right)
		node.maxPath = node.value + max(leftMax, rightMax)
		return node.maxPath

	def getMaxPathSum(self):
		return self.__getMaxPathSumHelper(self.triangle)

triangle = '75\n' + \
		   '95 64\n' + \
		   '17 47 82\n' + \
		   '18 35 87 10\n' + \
		   '20 04 82 47 65\n' + \
		   '19 01 23 75 03 34\n' + \
		   '88 02 77 73 07 63 67\n' + \
		   '99 65 04 28 06 16 70 92\n' + \
		   '41 41 26 56 83 40 80 70 33\n' + \
		   '41 48 72 33 47 32 37 16 94 29\n' + \
		   '53 71 44 65 25 43 91 52 97 51 14\n' + \
		   '70 11 33 28 77 73 17 78 39 68 17 57\n' + \
		   '91 71 52 38 17 14 91 43 58 50 27 29 48\n' + \
		   '63 66 04 68 89 53 67 30 73 16 69 87 40 31\n' + \
		   '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

print TrianglePathSum(triangle).getMaxPathSum()

