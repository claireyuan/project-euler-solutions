"""
Project Euler
Problem 25: 1000-digit Fibonacci number

Answer: 4782
"""

def fibonacciGenerator():
	prev, cur = 0, 1
	while True:
		prev, cur = cur, prev+cur 
		yield prev

def getFirstNDigitFibonacci(n):
	if n == 0 or n == 1:
		return 1
	check = 10**(n-1)
	for i, fib in enumerate(fibonacciGenerator()):
		if fib / check > 0:
			return i+1, fib

print getFirstNDigitFibonacci(1000)


