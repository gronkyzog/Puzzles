from  eulertools import gcd


def calc_radius(a,b,c):
	k = (a+b+c)/2.
	r = ((k*(k-a)*(k-b)*(k-c))**0.5)/k
	return r


def generate_primative_60(rmax):
	for m in range(1,1000):
		for n in range(1,m):
			if gcd(m,n) > 1:
				continue
			a0 = m**2 - n**2
			b0 = 2*m*n - n**2
			c0 = m**2 - m*n + n**2
			if a0==b0:
				continue
			k = gcd(a0,gcd(b0,c0))
			a0,b0,c0 = a0/k,b0/k,c0/k
			for s in range(1,1000):
				a,b,c = s*a0,s*b0,s*c0
				r = s*(3**0.5/(2*k))*n*(m-n)
				if r<= 100:
					yield (a,b,c),(m,n,k,s)
				else:
					break



def generate_count(rmax):
	counter = 0
	mmax = int(rmax*8/(3**0.5))
	for m in range(1,mmax):
		for n in range(1,m/2+1):
			if gcd(m,n) > 1:
				continue
			a = m**2 - n**2
			b = 2*m*n - n**2
			c = m**2 - m*n + n**2
			if a==b:
				continue
			else:
				k = gcd(a,gcd(b,c))
				r = (3**0.5/(2*k))*n*(m-n)
				if r<= rmax:
						bump = int(rmax/r)
						print m,n,k,bump
						counter += bump
				
				#else:
				#	break

	return counter
				



#a*n*(m-n)
#peak=a*(m-2*n)

print generate_count(10000)
