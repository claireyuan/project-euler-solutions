"""
Project Euler
Problem 9: Special Pythagorean triplet

Answer: 31875000
"""

def pythagoreanTripletAddUpTo(target):
	"""
	Returns a Pythagorean triplet that adds up to target if one exists, else
	returns None. Tries all triplets that add up to target.
	"""
	for c in xrange(target):
		for b in xrange(target - c):
			a = target - b - c
			if a**2 + b**2 == c**2:
				return a, b, c
	return None, None, None

def main():
	a, b, c = pythagoreanTripletAddUpTo(1000)
	if a is None:
		raise "Failed"
	print a*b*c

if __name__ == "__main__":
	main()