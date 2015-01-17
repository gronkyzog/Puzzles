
def primesieve(n):
    # return all primes <= n
    A = [0 for i in range(0,n+1)]
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]


print sum(primesieve(2000000))

print primesieve(10)