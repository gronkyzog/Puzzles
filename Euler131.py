def primeseive(n):
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


P = set(primeseive(10**6))

s = 1
counter = 0
while True:
    p = (s+1)**3 - s**3
    if p > 10**6:
        break
    if p in P:
        counter +=1
        print counter,p
    s=s+1
