import numpy as np

'''
How many games would we expect to be needed to complete a best-of-seven 
series if each team has a 50 percent chance of winning each individual 
game? How about if one team has a 60 percent chance of winning each game? 
How about 70?

From: https://fivethirtyeight.com/features/how-much-should-you-bid-for-that-painting/
'''

x1=np.random.uniform(0,100)
x2=np.random.uniform(0,100)

def series(p=.5):
	team1=0
	team2=0
	while team1<4 and team2 <4:
		result = np.random.uniform(0,1)
		if result > p:
			team1 +=1
		else:
			team2 +=1
	return (team1+team2)

def many_series(n=10000, p =.5):
	tote=0.0
	for _ in xrange(n):
		tote+=series(p)
	return tote/n

print("prob 0.5: %f" %many_series(10000000, p=.5))
print("prob 0.6: %f" %many_series(10000000, p=.6))
print("prob 0.7: %f" %many_series(10000000, p=.7))



