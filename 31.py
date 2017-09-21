"""
Project Euler
Problem 31: Coin sums

Answer: 73682
"""

coinValues = [1, 2, 5, 10, 20, 50, 100, 200]

class CoinSums:
	def __init__(self, coinValues):
		self.coinValues = coinValues
		self.sumMethods = {0: [[]]}

	def __addMethod(self, combinations, value):
		"""
		Stores unique combinations of coins that add up to value.
		"""
		for combination in combinations:
			combination.sort()
			if value not in self.sumMethods:
				self.sumMethods[value] = [combination]
			elif combination not in self.sumMethods[value]:
				self.sumMethods[value].append(combination)

	def waysToMakeValue(self, totalPence):
		"""
		Calculates the number of unique ways to make totalPence using any number of
		coins (British currency).
		"""
		# print totalPence, self.sumMethods
		if totalPence < 0:
			return 0
		if totalPence == 0:
			return 1
		if totalPence not in self.sumMethods:
			for coin in self.coinValues:
				if totalPence - coin >= 0:
					ways = self.waysToMakeValue(totalPence - coin)
					newWays = [combination + [coin] for combination in self.sumMethods[totalPence - coin]]
					self.__addMethod(newWays, totalPence)

		return len(self.sumMethods[totalPence])

print CoinSums(coinValues).waysToMakeValue(200)

	