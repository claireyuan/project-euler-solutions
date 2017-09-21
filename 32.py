"""
Project Euler
Problem 32: Pandigital products

Answer: 45228
"""
import math

class PandigitalProducts:
	def __init__(self):
		self.pandigitalProducts = set()

	def __isProduct(self, product, multiplicand, multiplier):
		return int(''.join(multiplicand)) * int(''.join(multiplier)) == int(''.join(product))

	def __recurProduct(self, product, multiplicand, multiplier):
		"""
		Checks every possible product to see if it is a pandigital product. 
		Invariant: Product, multiplicand, and multiplier together must be 
		pandigital.
		"""
		if len(product) >= 3:
			for digit in multiplier:
				if self.__recurMultiplicand(product, multiplicand, multiplier):
					self.pandigitalProducts.add(int(''.join(product)))
					break

		for digit in multiplier:
			newMultiplier = [d for d in multiplier if d != digit]
			self.__recurProduct(product + [digit], multiplicand, newMultiplier)

	def __recurMultiplicand(self, product, multiplicand, multiplier):
		"""
		With a fixed product, varies the multiplicand to try to make 
		multiplicand*multiplier == product. 
		Invariant: Product, multiplicand, and multiplier together must be 
		pandigital.
		""" 
		if len(product) > 0 and len(multiplicand) > 0 and len(multiplier) > 0:
			if self.__isProduct(product, multiplicand, multiplier):
				return True

		for digit in multiplier:
			newMultiplier = [d for d in multiplier if d != digit]
			if self.__recurMultiplicand(product, multiplicand + [digit], newMultiplier):
				return True
		return False

	def sumPandigitalProducts(self):
		"""
		Finds the sum of all products whose multiplicand/multiplier/product 
		identity can be written as a 1 through 9 pandigital.
		"""
		self.__recurProduct([], [], list('123456789'))
		return sum(self.pandigitalProducts)


print PandigitalProducts().sumPandigitalProducts()



