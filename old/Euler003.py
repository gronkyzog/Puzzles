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


x = 600851475143
rootx = int(x**0.5)
A = primesieve(rootx)
print len(A)
for z in A:
	if  x % z ==0:
		print z

