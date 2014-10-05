import eulertools




def primeseive(lb,ub):
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
	return primeseive(lb,ub)

#S(5678027) + S(7208785)

#A =  primes_row(7208785)


def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]


print len(primes(10**7))
#print len(eulertools.primeseive(10**7))

