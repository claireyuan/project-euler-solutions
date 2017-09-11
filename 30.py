"""
Project Euler
Problem 30: Digit fifth powers

Answer: 443839
"""

def sumOfDigitNthPowers(num, power):
	"""
	Takes each digit in num, raises them to power, and sums them.
	"""
	summ = 0
	while num > 0:
		summ += (num % 10) ** power
		num /= 10 
	return summ

def digitNthPowers(power, upperBound):
	"""
	Sums all integers from 10 to upperBound (non-inclusive) that can be written
	as the sum of nth powers of their digits.
	"""
	summ = 0
	for num in xrange(10, upperBound):
		if sumOfDigitNthPowers(num, power) == num:
			summ += num
	return summ

# Upper bound determined by trial and error
print digitNthPowers(5, 1000000)