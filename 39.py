"""
Project Euler
Problem 39: Integer right triangles

Answer: 840
"""
import math

def integerRightTrianglesWithPerimeterLessThan(maxPerimeter):
	"""
	Returns a map of perimeter value to integer right triangles with that
	perimeter.
	"""
	perimeterToRightTriangleSidesMap = {}
	for a in xrange(1, maxPerimeter - 2):
		b = a
		c = math.sqrt(a**2 + b**2)
		int_c = int(c)
		perimeter = a + b + int_c
		while perimeter < maxPerimeter:
			if a**2 + b**2 == int_c**2:
				if perimeter in perimeterToRightTriangleSidesMap:
					perimeterToRightTriangleSidesMap[perimeter] += 1
				else:
					perimeterToRightTriangleSidesMap[perimeter] = 1
			b += 1
			c = math.sqrt(a**2 + b**2)
			int_c = int(c)
			perimeter = a + b + int_c
	return perimeterToRightTriangleSidesMap

def getPerimeterWithMaxIntegerRightTriangles(upperBound):
	"""
	Returns the perimeter < upperBound with the most integer right triangles
	whose sides add up to it.
	"""
	perimeterToRightTriangleSidesMap = integerRightTrianglesWithPerimeterLessThan(upperBound)
	return max(perimeterToRightTriangleSidesMap.iterkeys(), key=(lambda key: perimeterToRightTriangleSidesMap[key]))

print getPerimeterWithMaxIntegerRightTriangles(1000)
