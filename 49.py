"""
Project Euler
Problem 49: Prime permutations

Answer: 296962999629
"""
import math

def update(dictionary, key, value):
	"""
	Adds value to the list at dictionary[key] if key already in dictionary.
	Otherwise adds key to the dictionary with [value].
	"""
	if key in dictionary:
		dictionary[key].append(value)
	else:
		dictionary[key] = [value]

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

def containsArithmeticSequence(numList):
	"""
	Returns True and the sequence if there exists a three number arithmetic 
	sequence in numList. Returns False and None otherwise.
	"""
	for i, firstElem in enumerate(numList):
		for j in xrange(i + 1, len(numList)):
			secondElem = numList[j]
			thirdElem = secondElem + (secondElem - firstElem)
			if thirdElem in numList:
				return True, [firstElem, secondElem, thirdElem]
	return False, None

def primePermutations():
	"""
	Prints the 12-digit numbers formed by concatenating the three terms in the 
	arithmetic sequence of 4-digit numbers in which each of the three numbers is
	prime and permutations of each other.
	"""
	primes = {}
	for i in xrange(1000, 10000):
		if isPrime(i):
			update(primes, ''.join(sorted(str(i))), i)

	for key in primes:
		isSequence, sequence = containsArithmeticSequence(primes[key])
		if isSequence:
			print ''.join(map(str, sequence))

primePermutations()
