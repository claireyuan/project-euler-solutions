"""
Project Euler
Problem 20: Factorial digit sum

Answer: 648
"""

class FactorialDigitSum:
	"""
	Stores the value of each intermediate factorial to speed up repeated calls 
	to factorialDigitSum.
	"""
	def __init__(self):
		self.factorialList = [[1]]

	def __multiply(self, multiplier, digitList):
		"""
		Multiplies two integers where multiplier is an int and digitList is an 
		integer represented as a list of digits from least significant to most
		significant.
		"""
		numList = []
		for i, digit in enumerate(digitList):
			product = digit * multiplier
			numList.append(self.__toDigitList(product, i))
		return self.__add(numList)

	def __add(self, numList):
		"""
		Adds all the integers in numList where each element of numList is an 
		integer represented as a list of digits from least significant to most 
		significant.
		"""
		ans = [0]
		for digitList in numList:
			carry = 0
			for i, digit in enumerate(digitList):
				if i < len(ans):
					summ = ans[i] + digit + carry
					ans[i] = summ % 10
					carry = summ / 10
				else:
					summ = carry + digit
					ans.append(summ % 10)
					carry = summ / 10
			while carry > 0:
				ans.append(carry % 10)
				carry /= 10
		return ans

	def __toDigitList(self, num, place):
		"""
		Converts an integer*(10^place) to its representation as a list of digits
		from least significant to most significant.
		"""
		digitList = [0] * place
		while num > 0:
			digitList.append(num % 10)
			num /= 10
		return digitList

	def factorialDigitSum(self, n):
		"""
		Adds up the digits of n!
		"""
		ans = [1]
		for i in xrange(n+1):
			if i < len(self.factorialList):
				ans = self.factorialList[i]
			else:
				ans = self.__multiply(i, ans)
				self.factorialList.append(ans)
		return sum(self.factorialList[n])

print FactorialDigitSum().factorialDigitSum(100)

