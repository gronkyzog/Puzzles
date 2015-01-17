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

def factorsieve(n):
    A = [[] for i in range(n+1)]
    for p in range(2,n+1):
        for s in range(p,n+1,p):
            A[s].append(p)
    return A

def factors(n,P):
    A = [[] for i in range(n+1)]
    for p in P:
        for s in range(p,n+1,p):
            A[s].append(p)
    return A


P = primesieve(10**5)
FS = factorsieve(10**5)
F = factors(10**5,P)

total = sum(P)
for p in P:
    if p > 5:
        A = FS[p-1]
        for f in A:
            if pow(10,f,p)==1:
                if set(F[f]).issubset(set([2,5])):
                    print p,f,F[f]
                    total -= p
                    break
print total
       
