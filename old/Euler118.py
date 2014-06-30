def prime_sieve(n):
    output = [0 for i in xrange(0,n+1)]
    output[0]=1
    output[1]=1
    output[2]=0
    for x in xrange(4,n+1,2):
        output[x]=1
    for s in xrange(3,n+1,2):
        for x in xrange(2*s,n+1,s):
            output[x]=1
    return [i for i,x in enumerate(output) if x ==0]


P = prime_sieve(10**8)
print len(P)

