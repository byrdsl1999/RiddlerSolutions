from scipy.misc import comb

def blast(n):
	tote=0.0
	for k in xrange(2,n+1):
		tote += (comb(n-k, 2)+comb(k-2, 2))/comb(n-2,2)
	return tote/(n-1)
  
