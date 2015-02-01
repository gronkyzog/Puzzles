# try to solve (p-r)*(q-r) = 1+r**2
# factorise 1+r**2 over primes P, use x = mod_sqrt(-1,p) to get all prime factors
# find solutions r<p<q , r < soln**(1/3)
# assume that solution is no bigger than 150000**3 

import itertools 
import eulertools

def factors(x,P):
	# for a geven set of primes which divide x, generate all factors of x
	
	if x == 1:
		return [1]
	r = x
	N = [0 for p in P]
	for i,p in enumerate(P):
		counter = 0
		while r % p ==0:
			r = r/p
			counter +=1
		N[i]=counter
	F = []
	Powers=[range(n+1) for n in N]
	for  E in itertools.product(*Powers):
		f = eulertools.product([p**e for p,e in zip(P,E)])
		F.append(f)
	return F

def alexandrian(n):
	R = [r**2 + 1 for r in range(n+1)]
	P = eulertools.primesieve(n)
	R = [[] for r in range(n+1)]
	for p in P:
		soln = eulertools.modsqrt_prime(-1,p)
		for s in soln:
			for k in xrange(s,n+1,p):
				r2 = k**2 +1
				R[k].append(p)
	
	F = []
	for r,V in enumerate(R):
		r2 = r**2 +1
		F.append(factors(r2,V))

				 

	output = set()
	for r,X in enumerate(F):
		if r==0:
			continue
		r2 = r**2 +1
		for x in X:
			p = x+r
			q = (r2/x) + r
			A = abs(r*p*q)
			if p*q - p*r - q*r != 1:
				raise
			output.add(A)

	return sorted(list(output))


def alexandrian2(n):
	output = set()
	for p in range(1,n):
		for q in xrange(p+1,2*p+1):
			r,s = divmod(1+p*q,q-p)
			if s==0:
				if r < q:
					raise
				A = p*q*r
				if A == 342108:
					print p,q,r
				output.add(A)

	return sorted(list(output))


n =150000
A =  alexandrian(n)
print len(A)
print A[n-1]
print 1884161251122450

