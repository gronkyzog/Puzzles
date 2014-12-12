import numpy
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


def radicals(n):
    P = primesieve(n)
    output = [1 for i in range(0,n+1)]
    for p in P:
        for s in range(p,n+1,p):
            output[s] *= p
    return output


R = radicals(100000)
A = [(r,i) for i,r in enumerate(R)]
A.sort()

print A[10000][1]
