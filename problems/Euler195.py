import eulertools


def calc_radius(a,b,c):
	k = (a+b+c)/2.
	r = ((k*(k-a)*(k-b)*(k-c))**0.5)/k
	return r


def generate_primative_60(rmax):
	for m in range(1,500):
		for n in range(1,m):
			if eulertools.gcd(m,n) >1:
				continue
			else:
				a = 4*m*n
				b = 3*m**2 + n**2
				c = 2*m*n + abs(3*m**2 - n**2)
				#a = m**2 - m*n + n**2
				#b = 2*m*n - n**2
				#c = m**2 - n**2
				#b**2 == a**2 + c**2 - a*c

				k = eulertools.gcd(a,eulertools.gcd(b,c))
				a0,b0,c0 = a/k,b/k,c/k
				if a0==b0==c0:
					continue

				for s in range(1,200):
					a,b,c = s*a0,s*b0,s*c0
					r = calc_radius(a,b,c)
					print r, ((1.*a*c)/(a+b+c))*(3**0.5)/2
					if r > 100:
						break
					else:	
						yield (m,n,s), [a,b,c,k,s]
output = set()
for i,(z,x) in enumerate(generate_primative_60(100),start=1):
	y = sorted(x)
	output.add(tuple(y))
	print i,x,len(output),z
