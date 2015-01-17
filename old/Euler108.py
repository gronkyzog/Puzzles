import math

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


q = 10**6
nprimes =   int(math.ceil(math.log(2.*(q-1) + 1.)/math.log(3.)))

P = primesieve(100)[:nprimes]

def product(A):
	total = 1
	for x in A:
		total *= x
	return total


P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,47]
maxn = product(P)
print maxn







