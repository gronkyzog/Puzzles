# For a given target,  perform repeated expanding by adding d + right rotated d
# this gives the position for each 2**n steps
# build all soutions 2^i  up to 2^(i-1) < x < 2**i
# recurvisily solve each residual  solve(x) = dMap[2**i] - Rotate solve(2**i-x)


def solve(x):
	if x in pMap:
		return pMap[x]
	n= x.bit_length()
	q = 2**n
	r = q - x
	(ax,ay) = pMap[q]
	(bx,by) = solve(r)
	return (ax-by,ay+bx)


D = (0,1)
pMap = {}
target = 10**12
n = target.bit_length()
for i in range(0,n+1):
	pMap[2**i] = D
	D = D[0]+D[1],D[1]-D[0]


print '%d,%d' %(solve(target))
