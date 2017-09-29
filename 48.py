"""
Project Euler
Problem 48: Self powers

Answer: 9110846700
"""

"""
Throughout this program, large numbers are represented as lists of digits, where
list[0] is the ones digit.
"""

def add(x, y):
	"""
	Adds y to x modulo 10 ^ (length of x).
	"""
	carry = 0
	for i, elem in enumerate(y):
		x[i], carry = (x[i] + elem + carry) % 10, (x[i] + elem + carry) / 10
	return x

def addAllMod(numList, modulus):
	"""
	Adds a list of ints modulo the 10^modulus so that the result is the last 
	modulus digits of the sum of all numbers in numList. Represents the result
	as a list of digits from least significant to most significant.
	"""
	ans = [0] * modulus
	for startPlace, num in enumerate(numList):
		if startPlace >= modulus:
			return ans
		carry = 0
		for i in xrange(startPlace, modulus):
			digit = (num % 10)
			summ = (ans[i] + digit + carry)
			ans[i], carry = summ % 10, summ / 10
			num /= 10
	return ans

def multMod(multiplicand, multiplier, modulus):
	"""
	Returns the least significant modulus digits of multiplicand * multiplier
	where multiplicand is an int as a list of digits and multiplier is an int.
	"""
	elements = []
	for i, digit in enumerate(multiplicand):
		elements.append(digit * multiplier)
	return addAllMod(elements, modulus)

def selfPowerMod(num, numDigits):
	"""
	Returns the last numDigits digits of num^num. Requires that num > 0.
	"""
	selfPower = add([0] * numDigits, [1])
	for i in xrange(num):
		selfPower = multMod(selfPower, num, numDigits)
	return selfPower

def selfPowerSeriesSum(numDigits, seriesLength):
	"""
	Returns the last numDigits of 1^1 + 2^2 + ... + seriesLength^seriesLength.
	"""
	ans = [0]*numDigits
	for i in xrange(1, seriesLength + 1):
		selfPowerMod(i, numDigits)
		add(ans, selfPowerMod(i, numDigits))
	strAns = ''.join(map(str, ans[::-1]))
	return strAns

print selfPowerSeriesSum(10, 1000)