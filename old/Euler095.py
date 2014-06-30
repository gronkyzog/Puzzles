import itertools 

def divisorsum(n):
    output = [1 for i in range(0,n+1)]
    for d in range(2,n):
        for s in range(2*d,n,d):
            output[s]+=d

    return output
n = 10**6
D = divisorsum(n)
print D[100]

max_cycle = 0
for i in range(2,n+1):
    cycle = set()
    x = i
    while True:
        if x > n:
            break
        if x in cycle:
            if x == i:
                ncycle = len(cycle)
                if ncycle > max_cycle:
                    print i,ncycle,min(cycle)
                    max_cycle = ncycle
            break
        else:
            cycle.add(x)
            x = D[x]







