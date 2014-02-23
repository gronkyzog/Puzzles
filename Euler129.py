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

maxk = 10**6

exitflag = False
for p in range(10**6,2*10**6):
    print p
    x = 1
    k = 1
    sol = set([x])
    while True:
        x = (x*10 + 1) % p
        k +=1
        if x in sol:
            break
        else:
            sol.add(x)
        if x ==0:
            if k > maxk:
                print p,x,k
                exitflag = True
            break


    if exitflag:
        break