from itertools import combinations
from eulertools import gcd,factorise,primesieve,product
r = 12017639147
#r = 1000001

h = (r+3)/2
P = primesieve(int(h**0.5)+1)
F = set(factorise(P,h))
N = len(F)
total = int(h/3)
print h,N,F
for k in range(1,N+1):
	for X in combinations(F,k):
		prod = product(X)
		term = int(2*h/(3*prod))- int(h/(3*prod))
		sign =  (-1)**k
		print X,k,sign,prod
		total += sign*term
		
		

print total
#print 80840



