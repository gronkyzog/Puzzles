
import itertools
def product(A):
    total = 1
    for a in A:
        total *= a
    return total

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)+1))




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



def factors(n,P):
    A = [[] for i in range(n+1)]
    for p in P:
        k = 1
        q = p
        while q <= n:
            for s in range(q,n+1,q):
                A[s].append(p)
            q = p*q
            k +=1
    B = []
    for a in A:
        sa = list(set(a))
        sa.sort()
        b = [(s,a.count(s)) for s in sa]
        B.append(b)
    return B



P = primesieve(10**6)
F = factors(10**6,P)

print 'start'
for k,f in enumerate(F):
    if k % 1000 ==0:
        print k
    k3 = k**3
    B = [s[0] for s in f]
    exponents = [range((3*s[1])/2+1) for s in f]
    for E in itertools.product(*exponents):
        n = product([b**e for b,e in zip(B,E)])
        n2 = n**2
        if k3 % n2 ==0:
            p = k3/n2 - n
            if p in P:
                print p,k,n,E,exponents
        else:
            raise Exception('WTF!')



