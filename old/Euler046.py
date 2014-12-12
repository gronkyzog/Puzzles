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

n = 10**4
P = primesieve(n)
A = [0 for i in range(0,n)]

for p in P:
	z = p
	i=0
	while True:
		z = p + 2*(i**2)
		if z < n:
			A[z]=1
			i=i+1
		else:
			break
B = [i for i in range(0,n) if A[i]==0 and i%2 ==1]
print B[:10]
