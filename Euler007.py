import numpy
import math
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


n = 10001 
max_size = int(n*math.log(n*math.log(n)))
A = primeseive(max_size)
print len(A),
print A[n-1],max_size
