import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom




for n in range(1,1000):
	A = [int(min(ncr(n,s) %7,1)) for s in range(0,n+1)]
	print n,sum(A)