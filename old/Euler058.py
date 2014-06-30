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





def prime_count(x):
	tl =    4*x**2 +1
	tr =    4*x**2 -2*x + 1
	bl =    4*x**2 +2*x + 1
	return is_probable_prime(tl)+is_probable_prime(tr)+is_probable_prime(bl)


total = 0
for x in range(1,50000):
	z = prime_count(x)
	total = total + z
	s = 4*x + 1
	#print x,(2*x+1),z,total,s,(1.0*total)/s
	if (1.0*total)/s <= 0.1:
		print x,s,total,(1.0*total)/s
		print 'Sol:%d ' %(2*x+1)
		break
