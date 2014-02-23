import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


# for n in xrange(0,2000,1):
# 	A = [int(min(ncr(n,r) % 7,1)) for r in range(0,n+1)]
# 	print n,A


for r in range(0,1000):
	print r,ncr(10**9,r) % 7


