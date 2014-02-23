import numpy
def primeseive(n):
    # return all primes <= n
    A = numpy.zeros([n+1])
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]



n = 10**6
P = primeseive(n)
q = len(P)
sP = set(P)
for i in xrange(3,1000,2):
	A = [sum(P[s:s+i]) for s in range(0,q-i)]
	B = [p for p in A if p in sP]
	if len(B) > 0:
		print i,len(B),B[:10]

