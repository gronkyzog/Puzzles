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

def cycle(q):
    x =1
    k=1
    while True:
        x = (10*x + 1) % q
        k+=1
        if x ==0:
            return k



P = [p for p in primeseive(10**6) if p > 5]

counter = 0
total = 0
for p in P:
    x = cycle(p)
    if x > 0:
        if 10**9 % x ==0:
            counter +=1
            total += p
            print counter,total,p,x
            if counter ==40:
                break
    else:
        print 'WTF %d' %p







