import math
import itertools


def cycle(q,k):
    if k ==1:
        for i in range(q+1):
            yield [i]
    else:
        for i in range(q+1):
            for x in cycle(i,k-1):
                output = [i]
                output.extend(x)
                yield output

q = 10**6
nprimes =   int(math.ceil(math.log(2.*(q-1) + 1.)/math.log(3.)))


def primesieve(n):
    # return all primes <= n
    A = [0 for i in range(0,n+1)]
    for i in range(4,n+1,2):
                A[i]=1

    for i in range(3,n+1,2):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i): 
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]






def product(A):
    total = 1
    for x in A:
        total *= x
    return total



combin = 1000
nprimes = int(math.ceil(math.log(2*(combin-1) +1)/math.log(3)))
print nprimes
P = primesieve(1000)[:nprimes]



print P
minq = product(P)+1
n = len(P)
print 'Start'
i=0
for E in cycle(5,nprimes):
    i=i+1
    c = (product([2*e+1 for e in E])-1)/2 +1
    if c >=combin:
        q = product([p**e for p,e in zip(P,E)])
        if q < minq:
            print q,c,E
            minq = q

#print i
        






