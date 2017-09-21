"""
Project Euler
Problem 35: Circular primes

Answer: 55
"""
import math

class CircularPrimes:
	def __getRotations(self, num):
		"""
		Returns all rotations of num in a list.
		"""
		numAsStr = str(num)
		allRotations = []
		for starting_index in xrange(len(numAsStr)):
			curRotation = []
			for i in xrange(len(numAsStr)):
				curRotation.append(numAsStr[(starting_index + i) % len(numAsStr)])
			allRotations.append(int(''.join(curRotation)))
		return allRotations

	def __isPrime(self, num):
		"""
		Returns True if num is prime, False otherwise. Requires that num is an 
		int and positive.
		"""
		if num < 2:
			return False
		if num == 2:
			return True

		for i in xrange(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
		return True

	def __isCircularPrime(self, num):
		"""
		Returns True if num is a circular prime (if all rotations of num are 
		prime) and False otherwise.
		"""
		allRotations = self.__getRotations(num)
		for rotation in allRotations:
			if not self.__isPrime(rotation):
				return False, allRotations
		return True, allRotations

	def getCircularPrimes(self, upperBound):
		"""
		Returns a list of all circular primes less than the given upperBound.
		"""
		circularPrimes = set()
		checked = set()
		for i in xrange(2, upperBound):
			if i not in checked:
				isCircularPrime, rotations = self.__isCircularPrime(i)
				checked.update(rotations)
				if isCircularPrime:
					lessThanUpperBound = [rotation for rotation in rotations \
										  if rotation < upperBound]
					circularPrimes.update(lessThanUpperBound)
		return circularPrimes

print len(CircularPrimes().getCircularPrimes(1000000))



