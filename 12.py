"""
Project Euler
Problem 12: Highly divisible triangular number

Answer: 76576500
"""
import math

def triangularNumberGenerator():
	"""
	Generator that generates triangle numbers.
	"""
	i = 1
	num = 0
	while True:
		num += i
		i += 1
		yield num

def numDivisors(num):
	"""
	Returns the number of divisors of num.
	"""
	divisors = set()
	for i in xrange(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			divisors.add(i)
			divisors.add(num/i)
	return len(divisors)

def getFirstTriangleNumberOverTargetDivisors(target):
	""" 
	Gets the first triangle number that has number of divisors >= target.
	"""
	triangularNumGenerator = triangularNumberGenerator()
	triangularNum = triangularNumGenerator.next()
	curNumDivisors = numDivisors(triangularNum)
	while curNumDivisors < target:
		triangularNum = triangularNumGenerator.next()
		curNumDivisors = numDivisors(triangularNum)
	return triangularNum

print getFirstTriangleNumberOverTargetDivisors(500)