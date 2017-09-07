"""
Project Euler
Problem 21: Amicable numbers

Answer: 31626
"""
import math

def d(n):
	"""
	Returns the sum of proper divisors of n.
	"""
	divisors = set([1])
	for i in xrange(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n / i)
	return sum(divisors)

def sumAmicableNumbers(upperBound):
	"""
	Sums all the amicable numbers under upperBound.
	"""
	summ = 0
	for a in xrange(1, upperBound):
		b = d(a)
		if a != b and d(b) == a:
			summ += a
	return summ

print sumAmicableNumbers(10000)