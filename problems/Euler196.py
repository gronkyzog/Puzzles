import eulertools




def primesieve(lb,ub):
	# find all primes in range [lb,ub] inclusive
	N = ub-lb
	A = [1 for x in xrange(N+1)]
	#A[0]=0
	#A[1]=0
	p=2
	k,r = divmod(lb,p)
	if r!= 0:
		k+=1
	k = max(k,2)
	for s in xrange(k*p-lb,N+1,p):
		A[s]=0

	pub = int(ub**0.5)
	for p in xrange(3,pub+1,2):
		k,r = divmod(lb,p)
		if r!= 0:
			k+=1
		k = max(k,2)
		#print p,k,lb,k*p,ub
		offset = k*p-lb

		for s in xrange(offset,N+1,p):
			A[s]=0

	return lb,A
		


def primes_row(n):
	lb = n*(n-1)/2 +1
	ub = lb+n-1
	return primesieve(lb,ub)

#S(5678027) + S(7208785)

#A =  primes_row(7208785)

def prime_tripples(n):
	L1,A1 = primes_row(n-2)
	L2,A2 = primes_row(n-1)
	L3,A3 = primes_row(n)
	L4,A4 = primes_row(n+1)
	L5,A5 = primes_row(n+2)
	
	A = [A1,A2,A3,A4,A5]


prime_tripples(8)


