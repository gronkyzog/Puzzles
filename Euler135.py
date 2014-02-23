#16*b^2 - 20*n  must be a perfect square
# (4b + n)
#(4b)^2 - c**2 = 20*n


def factors(n):
    A = [[] for i in range(n+1)]
    for p in range(1,n+1):
        for s in range(p,n+1,p):
            A[s].append(p)
    return A



F = factors(10**6)
print 'GenerationComplete'
total = 0
for x in range(1150,10**6+1):
	A = F[x]
	factors = [tuple([a,20*x/a]) for a in A]
	factors.extend([tuple([2*a,10*x/a]) for a in A])
	factors.extend([tuple([4*a,5*x/a]) for a in A])
	factors.extend([tuple([10*a,2*x/a]) for a in A])
	factors.extend([tuple([10*a,2*x/a]) for a in A])
	factors = list(set(factors))
	counter = 0
	for f in factors:
		b8 = f[0]+f[1]
		c2 = f[1]-f[0]
		if b8 % 8 == 0 and c2 % 2 ==0:
			b = b8/8
			c = c2/2
			if c > 0:
				if (-6*b + c) % 10 ==0:
					a = (-6*b + c)/10
					if 2*a + b > 0:
						counter +=1
	if counter ==10:
		total +=1
		print total,x,counter,len(factors)
print total