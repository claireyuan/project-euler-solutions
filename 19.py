"""
Project Euler
Problem 19: Counting Sundays

Answer: 171
"""

def numDays(month, year):
	"""
	Returns the number of days in the given month in the given year.
	"""
	if month in [9, 4, 6, 11]:
		return 30
	elif month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return 29
	elif month == 2:
		return 28
	else:
		return 31

def countSundaysFirstOfMonth(startYear, endYear):
	"""
	Counts the number of Sundays that fell on the first of the month in the 
	given range [startYear, endYear]. 
	Requires startYear >= 1900 and endYear > startYear.
	"""
	dayOfWeek = 1
	numSundays = 0
	for year in xrange(1900, endYear + 1):
		for month in xrange(1, 13):
			if year >= startYear and dayOfWeek == 0:
				numSundays += 1
			dayOfWeek += numDays(month, year)
			dayOfWeek %= 7
	return numSundays

print countSundaysFirstOfMonth(1901, 2000)
