from itertools import combinations,permutations

import random
import numpy
from random import randint


_mrpt_num_trials = 10 # number of bases to test
 
def is_probable_prime(n):
    if n == 1:
        return False
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


def build_number(dx):
	return sum([s*(10**i) for i,s in enumerate(dx[::-1])])

def build_primes(A):
    n = len(A)
    output = []
    for i in range(1,n+1):
        x = build_number(A[:i])
        if is_probable_prime(x):
            dy = A[i:]
            if len(dy)==0:
                temp = [x]
                output.append(temp)
                return output
            else:
                for z in build_primes(dy):
                    temp = [x]
                    temp.extend(z)
                    output.append(temp)
    return output


output = set()
A = [i for i in range(1,10)]

#temp = build_primes([2,5,4,7,8,9,6,3,1])
#print temp

for X in permutations(A):
    if X[-1] in (2,4,6,8):
        continue
    temp = build_primes(X)
    if len(temp)>0:
        for z in temp:
            z.sort()
            print X,z
            output.add(tuple(z))

print len(output)






