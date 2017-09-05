"""
Project Euler
Problem 16: Power digit sum

Answer: 1366
"""

def power(base, exp):
	"""
	Do the exponentiation as a list of digits to avoid integer overflow. Returns
	base**exp as a list of digits from least significant to most significant.
	"""
	ans = [1]
	while exp > 0:
		carry = 0
		for i in xrange(len(ans)):
			mult = ans[i] * base + carry
			ans[i] = mult % 10
			carry = mult / 10
		while carry > 0:
			ans.append(carry % 10)
			carry /= 10
		exp -= 1
	return ans

def powerDigitSum(base, exp):
	"""
	Adds the digits of base**exp.
	"""
	return sum(power(base, exp))
	
print powerDigitSum(2, 1000)



