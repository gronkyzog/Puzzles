import itertools
import eulertools
Q = 2**25
N = Q**2
P = eulertools.primeseive(Q)

print 'Primes Generated'
M = eulertools.mobius(Q,P)
print 'Mobius Generated'


total = 0
for n in range(1,Q+1):
	total += M[n]*(N/(n*n))

print total
print Q - total

