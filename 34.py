"""
Project Euler
Problem 34: Digit factorials

Answer: 40730
"""

class DigitFactorials:
	def __init__(self):
		self.factorials = [1, 1, 2]

	def __factorial(self, num):
		"""
		Calculates and stores (num!).
		"""
		if num < len(self.factorials):
			return self.factorials[num]
		ans = num * self.__factorial(num - 1)
		self.factorials.append(ans)
		return ans

	def digitFactorial(self, num):
		"""
		Calculates the sum of the factorials of each digit of num.
		"""
		summ = 0
		while num > 0:
			summ += self.__factorial(num % 10)
			num /= 10
		return summ

d = DigitFactorials()
summ = 0
# Range determined by trial and error
for i in xrange(3, 100000):
	if i == d.digitFactorial(i):
		summ += i
print summ