import math

def C(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))



A = [C(n,r) for n in range(0,101) for r in range(0,n+1)]
B = [a for a in A if a > 1000000]
print len(B)
