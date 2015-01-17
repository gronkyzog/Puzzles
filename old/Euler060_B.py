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


def primeCombin(Y,x,P):
	for y in Y:
		xy = int(str(x)+str(y))
		yx = int(str(y)+str(x))
		if xy not in P  or yx not in P:
			return False

	return True

def primesieve(n):
    # return all primes <= n
    A = [0 for i in xrange(0,n+1)]

    for i in xrange(4,n+1,2):
    	A[i]=1
    for i in xrange(6,n+1,3):
    	A[i]=1

    for i in xrange(3,n+1,2):
        if A[i]==1:
            continue
        else:
            for j in xrange(2*i,n+1,i):
                A[j]=1
    return [i for i in xrange(2,n+1) if A[i]==0]

SP = set(primesieve(10**8))
P = primesieve(10**4)
print 'Generating Primes Complete'
print len(P),len(SP)
n = len(P)

output = []
for i in range(n):
	for j in range(i+1,n):
		x,y = P[i],P[j]
		xy = int(str(x)+str(y))
		yx = int(str(y)+str(x))
		if xy in SP and yx in SP:
			output.append([x,y])

print len(output)


for i in range(3,6):
	temp = []
	for Y in output:
		for x in P:
			if x <= max(Y):
				continue
			if primeCombin(Y,x,SP):
				Z = list(Y)
				Z.append(x)
				temp.append(Z)
	output = list(temp)
	if len(output)>0:
		print i,len(output),output[0],sum(output[0])


