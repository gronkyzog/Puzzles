import numpy

def primesieve(n):
    # return all primes <= n
    A = numpy.zeros([n+1])
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]



def factors(P,n):
	A = numpy.zeros([n+1])
 	for p in P:
 		for s in xrange(p,n,p):
 			A[s]+=1
 	return A

n = 10**6
P = primesieve(n)
A = factors(P,n)
for i in range(1,len(A)-4):
	x0 = A[i]
	x1 = A[i+1]
	x2 = A[i+2]
	x3 = A[i+3]
	if x0 ==4 and x1 ==4 and x2==4 and  x3 ==4:
		print i
		break

