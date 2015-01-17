import eulertools


def totent_chain(x):
	counter = 1
	while x!=1:
		x = A[x]
		counter +=1
	return counter

n = 40*10**6

P = eulertools.primesieve(n)


A = [i for i in xrange(n+1)]

for p in P:
	for s in xrange(p,n+1,p):
		A[s] *= (p-1)
		A[s] /=p

print 'Go'
total = 0
for p in P:
	length = totent_chain(p)
	if length==25:
		total +=p

print total