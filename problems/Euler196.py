import eulertools




def primeseive(lb,ub):
	# find all primes in range [lb,ub] inclusive
	N = ub-lb
	A = [0 for x in xrange(N+1)]

	p=2
	k,r = divmod(lb,p)
	if r!= 0:
		k+=1
	k = max(k,2)
	for s in xrange(k*p-lb,N+1,p):
		A[s]=1

	pub = int(ub**0.5)
	for p in xrange(3,pub+1,2):
		k,r = divmod(lb,p)
		if r!= 0:
			k+=1
		k = max(k,2)
		#print p,k,lb,k*p,ub
		offset = k*p-lb
		for s in xrange(offset,N+1,p):
			A[s]=1

	return [i for i,a in enumerate(A,start=lb) if a==0]
		


row=8*10**6
lb = row*(row+1)/2
ub = (row+5)*(row+6)/2
P = primeseive(lb,ub)
print len(P)