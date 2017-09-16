import numpy as np

'''
From Max Weinreich, a purge puzzle:

A town of 1,000 households has a strange law intended to prevent wealth-hoarding. On January 1 of every year, 
each household robs one other household, selected at random, moving all of that house’s money into their own 
house. The order in which the robberies take place is also random and is determined by a lottery. (Note that 
if House A robs House B first, and then C robs A, the houses of A and B would each be empty and C would have
acquired the resources of both A and B.)

Two questions about this fateful day:

    What is the probability that a house is not robbed over the course of the day?
    
    Suppose that every house has the same amount of cash to begin with — say $100. Which position in the 
    lottery has the most expected cash at the end of the day, and what is that amount?
'''

class house(object):
	def __init__(self, name='house'):
		self.name=name
		self.loot = 100
	def __repr__(self):
		return str(self.name)

class town(object):
	def __init__(self, size=1000):
		self.houses = []
		for _ in range(size):
			self.houses.append(house(_))

	def reset(self):
		for house in self.houses:
			house.loot = 100

	def rob(self, houseA, houseB):
		houseA.loot += houseB.loot
		houseB.loot = 0

	def rob_all(self):
		order = np.random.choice(self.houses, len(self.houses), False)
		for house in order:
			target = np.random.choice(self.houses, 1)[0]
			while target == house:
				target = np.random.choice(self.houses, 1)[0]
			#print house, house.loot
			#print target, target.loot
			self.rob(house, target)

	def report_valuables(self):
		return np.array([house.loot for house in self.houses])

if __name__ == '__main__':
	TRIALS = 10000
	SIZE = 100
	results = []
	t=town(SIZE)
	not_robbed=0.0
	for _ in range(TRIALS):
		t.rob_all()
		results.append(t.report_valuables())
		if _ ==0:
			result_array = np.array(t.report_valuables())
		else:
			result_array += np.array(t.report_valuables())
		t.reset()
		if _%100 ==0: 
			print _ 
