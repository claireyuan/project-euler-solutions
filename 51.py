"""
Project Euler
Problem 51: Prime digit replacements

Answer: 121313
"""
import math

class PrimeDigitReplacements:
	def __init__(self):
		self.prev = [2]
		self.cur = -1

	def __isPrimeNaive(self, num):
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

	def __isPrimeUsingPrevPrimes(self, num):
		"""
		Checks primality by testing only the previously generated primes as 
		potential divisors.
		"""
		if num == 2 or num == 3:
			return True
		if num % 2 == 0 or num < 2:
			return False

		for prime in self.prev:
			if num % prime == 0:
				return False
		return True

	def __replaceDigits(self, digit, numAsArr):
		"""
		Returns a list of all numbers made by replacing every instance of digit
		in numAsArr with 0-9
		"""
		result = []
		for i in xrange(0, 10):
			if numAsArr[0] != digit or i > 0:
				tmp = 0
				for d in numAsArr:
					if d == digit:
						tmp = (tmp*10) + i
					else:
						tmp = (tmp*10) + d
				result.append(tmp)
		return result


	def __getMaxFamilySize(self, num):
		"""
		Gets the largest prime family gotten by replacing all instances of a 
		digit with all 0-9.
		"""
		numAsArr = map(int, str(num))
		maxSize = 0
		for digit in numAsArr:
			generated = self.__replaceDigits(digit, numAsArr)
			primeFamily = filter(self.__isPrimeNaive, generated)
			maxSize = max(maxSize, len(primeFamily))
		return maxSize

	def solveProblem(self, primeFamilySize):
		i = 2
		while True:
			if self.__isPrimeUsingPrevPrimes(i):
				self.prev.append(i)
				if self.__getMaxFamilySize(i) >= primeFamilySize:
					return i
			i += 1

print PrimeDigitReplacements().solveProblem(8)

