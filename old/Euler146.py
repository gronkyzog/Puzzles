import random
import numpy
from random import randint

_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite





def product(A):
    total = 1
    for a in A:
        total *= a
    return total

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




nmax = 150*10**6
P = primesieve(17)
prodP = product(P)
C = [1,3,7,9,13,27]
D = [d for d in range(2,27) if d not in C]
trials =[]
for n in xrange(2,prodP+1,2):
    insertflag = True
    for c in C:
        f = n**2 + c
        for p in P:
            q,r = divmod(f,p)
            if r==0 and q>1:
                insertflag = False
                break
        if not insertflag:
            break
    if insertflag:
        trials.append(n)

print len(trials)

A = []
for t in trials:
    n = t
    while n <= nmax:
        A.append(n)
        n += prodP

A.sort()


print len(A)
for c in C:
    A = [a for a in A if is_probable_prime(a**2 + c)]
    print c,len(A)

for d in D:
    A = [a for a in A if not is_probable_prime(a**2 + d)]
    print d,len(A)



print ('Start')
for a in A:
    print a
print sum(A)
