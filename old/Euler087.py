import itertools
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

n = 50000000
rootn = int(n**0.5)
P = primeseive(rootn)
print len(P)

scoreMap = {}
counter = 0
n = 50000000

print 'Starting'
output = []
for x in P:
    for y in P:
        w = x**2 + y**3 
        if w > n:
            break
        for z in P:
            total = w + z**4
            if total > n:
                break
            output.append(total)
output = set(output)
print len(output)            
