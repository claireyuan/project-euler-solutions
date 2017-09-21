"""
Project Euler
Problem 33: Digit cancelling fractions

Answer: 100
"""

def cancelDigits(numerator, denominator):
	"""
	Naively cancels the digits in common between the numerator and denominator.
	If numerator and denominator are equal, returns (0,0). Requires numerator
	and denominator to be strings.
	"""
	for digit in numerator:
		if digit in denominator and digit != '0':
			n = list(numerator)
			n.remove(digit)
			d = list(denominator)
			d.remove(digit)
			return cancelDigits(''.join(n), ''.join(d))
	try:
		return int(numerator), int(denominator)
	except:
		return 0, 0

def simplifyFraction(numerator, denominator):
	"""
	Simplifies numerator and denominator to their simplest form.
	"""
	for i in xrange(2, min(numerator, denominator) + 1):
		if numerator % i == 0 and denominator % i == 0:
			return simplifyFraction(numerator / i, denominator / i)
	return numerator, denominator

def muliplyFractions(fractions):
	"""
	Given a list of fractions in the form (numerator, denominator), multiplies
	them together and returns the answer in simplest form as 
	(numerator, denominator).
	"""
	n = 1
	d = 1
	for numerator, denominator in fractions:
		n *= numerator
		d *= denominator
	return simplifyFraction(n, d)

def productDigitCancellingFractionDenominators():
	"""
	Returns the product of all non-trivial examples of fractions, less than one
	in value, and containing two digits in the numerator and denominator, which
	when simplified naively (by cancelling digits) produces the correct 
	simplication.
	"""
	funFractions = []
	for denominator in xrange(11, 100):
		for numerator in xrange(10, denominator):
			naiveSimplify = cancelDigits(str(numerator), str(denominator))
			realSimplify = simplifyFraction(numerator, denominator)
			if naiveSimplify != (numerator, denominator):
				naiveSimplify = simplifyFraction(naiveSimplify[0], naiveSimplify[1]) 
				if naiveSimplify == realSimplify:
					funFractions.append((numerator, denominator))
	return muliplyFractions(funFractions)

print productDigitCancellingFractionDenominators()