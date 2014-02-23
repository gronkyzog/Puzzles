import itertools
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



def generate_primes(n,s,k):
    output = []
    for X in itertools.combinations(range(n),k):
        S = [s for i in range(n)]
        for Z in itertools.product(range(10),repeat=k):
            if s in Z:
                continue
            for x,z in zip(X,Z):
                S[x] = z
            q = sum([z*10**i for i,z in enumerate(S)])
            if q < 10**(n-1):
                continue
            if is_probable_prime(q):
                #print q,S
                output.append(q)
    return output

total = 0
for s in range(10):
    i = 1
    while True:
        primes = generate_primes(10,s,i)
        total += sum(primes)
        if len(primes) > 0:
            break
        i+=1
    print s,10-i,len(primes),sum(primes),total
  





