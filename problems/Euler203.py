from eulertools import primesieve
from math import factorial

def nCr(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))

def containsFactor(x,F):
	for f in F:
		if x % f ==0:
			return True
	return False

N = 51

P = primesieve(N)
F = [p**2 for p in P]
output = set([nCr(n,r)  for n in range(0,N) for r in range(0,n+1)])

output = [a for a in output if not containsFactor(a,F)]
print output
print len(output)
print sum(output)