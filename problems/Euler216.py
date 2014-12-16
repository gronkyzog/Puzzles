import eulertools
import numpy

nmax = 50*10**6

A = [0 for i in xrange(nmax+1)]

P = set(eulertools.primesieve(int(2**0.5*nmax)+1))
print len(P)
print 'Done'
for p in sorted(list(P)):
	if p>2:
		roots = eulertools.modsqrt_prime((p+1)/2,p)
		if len(roots)>0:
			for r in roots:
				if 2*r*r-1 in P:
					a = r+p
				else:
					a = r
				for s in xrange(a,nmax+1,p):
					A[s]=1
print nmax-sum(A)-1


