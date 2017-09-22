"""
Project Euler
Problem 42: Coded triangle numbers

Answer: 162
"""
import csv

class CodedTriangleNumbers:
	def __init__(self):
		self.triangleNumbers = [1]
		self.n = 1

	def __isTriangleNumber(self, num):
		"""
		Returns True if num is a triangle number, and False otherwise.
		"""
		if num < self.triangleNumbers[-1]:
			return num in self.triangleNumbers

		triangleNum = self.triangleNumbers[-1]
		while triangleNum < num:
			triangleNum = (self.n * (self.n + 1)) / 2
			self.triangleNumbers.append(triangleNum)
			self.n += 1
		return num == triangleNum

	def __wordValue(self, word):
		"""
		Adds the alphabetical position of each character in word.
		"""
		value = 0
		for char in word:
			value += ord(char) - ord('A') + 1
		return value

	def countTriangleWords(self, fileName):
		"""
		Counts the number of words in fileName whose word value is a triangle 
		number. Requires fileName to be comma-separated with double quotes around
		each all-uppercase word.
		"""
		numTriangleWords = 0
		with open(fileName, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			for line in reader:
				for word in line:
					if self.__isTriangleNumber(self.__wordValue(word)):
						numTriangleWords += 1
		return numTriangleWords

print CodedTriangleNumbers().countTriangleWords('42_words.txt')

