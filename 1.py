"""
Project Euler
Problem 1: Multiples of 3 and 5

Answer: 233168
"""

def allMultiplesOf3or5(upperBound):
	ans = 0
	for i in xrange(1, upperBound):
		if i % 3 == 0 or i % 5 == 0:
			ans += i
	return ans

print allMultiplesOf3or5(1000)