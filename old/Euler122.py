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



P = primeseive(10**6)

for i,p in enumerate(P,start=1):
    if i % 2 ==0:
        continue
    else:
        x = 2*i*p
        if x > 10**10:
            print i,p,x
            break

