"""
Project Euler
Problem 2: Even Fibonacci numbers

Answer: 4613732
"""

def sumEvenFibonacci(upperBound):
	ans = 0
	prev = 1
	cur = 1
	while cur <= upperBound:
		if cur % 2 == 0:
			ans += cur
		prev, cur = cur, cur + prev
	
	return ans

print sumEvenFibonacci(4000000)