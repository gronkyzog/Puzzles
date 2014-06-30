from itertools import *

def ulam2(v):
    b = [0]*v + [1]
    for t in count():
        b[t%(v+1)] ^= b[(t-1)%(v+1)]
        if b[t%(v+1)]: yield v + 2*t + 2
 
N = 32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152
D = 126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606
z = 10**11-3

t = 0
for v, n, d in izip(xrange(5, 22, 2), N, D):
    l = [0]*n
    for s, x in izip(count(), ulam2(v)):
        if x-l[s%n] == d and not (z-s-1)%n:
            t += x+d*(z-s-1)/n
            break
        l[s%n] = x
print t

