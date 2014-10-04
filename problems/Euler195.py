from  eulertools import gcd

def generate_count(rmax):
	counter = 0
	mmax = int(rmax*6/(3**0.5))+2
	for m in xrange(3,mmax):
		if m%1000==0:
			print m
		nmax = m/2+1
		for n in xrange(1,nmax):
			if gcd(m,n) > 1:
				continue

			k =gcd(m+n,2*m-n)
			r = (3**0.5/(2*k))*n*(m-n)
			if r<= rmax:
				bump = int(rmax/r)
				counter += bump
				#print m,n,bump
				
			elif r > 3*rmax:
				break

	return counter
				



print generate_count(1053779)
