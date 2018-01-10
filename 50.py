"""
Project Euler
Problem 50: Consecutive prime sum

Answer: 997651
"""
import math

def isPrime(num):
	"""
	Checks primality by testing all possible divisors up to the square root
	of num.
	"""
	if num == 2 or num == 3:
		return True
	if num % 2 == 0 or num < 2:
		return False

	for i in xrange(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True

def getPrimesUpTo(upperBound):
	"""
	Returns a list of all primes up to upperBound.
	"""
	primes = []
	for i in xrange(2, upperBound):
		if isPrime(i):
			primes.append(i)
	return primes

def consecutivePrimeSum(upperBound):
	"""
	Returns the prime < upperBound that can be written as the sum of the most
	consecutive primes.
	"""
	lo = 0
	curLongest, primeSum = 0, 0
	primes = getPrimesUpTo(upperBound)

	while lo < len(primes) - curLongest:
		curSum = 0
		hi = lo
		while hi < len(primes) and curSum < upperBound:
			curSum += primes[hi]
			if hi - lo > curLongest and curSum < upperBound and isPrime(curSum):
				curLongest, primeSum = hi - lo, curSum
			hi += 1
		lo += 1
	return primeSum

print consecutivePrimeSum(1000000)



