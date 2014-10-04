import eulertools




def primeseive(lb,ub):
	# find all primes in range [lb,ub] inclusive
	A = [0 for x in xrange(lb,ub+1)]

	p=2
	k,r = divmod(lb,p)
	k = max(k,2)
	for s in xrange(k*p,ub,p):
		w = s-lb
		A[w] = 1	

	for p in range(3,ub+1,2):
		#print p
		k,r = divmod(lb,p)
		k = max(k,3)
		for s in xrange(k*p,ub+1,p):
			print p,s
			w = s-lb
			A[w] = 1

	return [lb+i for i,a in enumerate(A) if a==0]

P = eulertools.primeseive(200)
P = [p for p in P if p   >100]
print primeseive(100,200)
print P






