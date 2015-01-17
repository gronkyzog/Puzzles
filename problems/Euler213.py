import numpy
nrows = 30
ncols = 30
npos  = nrows*ncols


mapper = {}
for r in xrange(nrows):
	for c in xrange(ncols):
		key = (r,c)
		possible = []
		if r >= 1:
			possible.append((r-1,c))
		if r < nrows-1:
			possible.append((r+1,c))
		if c >= 1:
			possible.append((r,c-1))
		if c < ncols-1:
			possible.append((r,c+1))
		mapper[key] = possible

A = numpy.zeros([npos,npos])

for k,v in mapper.items():
	y = k[1] + k[0]*ncols
	a = 1./len(v)
	for p in v:
		x = p[0] + p[1]*ncols
		A[x,y] = a 

#print A
A = numpy.linalg.matrix_power(A,50)


total = numpy.ones([npos])

for i in range(npos):
	print i,sum(total)
	x = numpy.zeros([npos])
	x[i]= 1.
	y = numpy.dot(A,x)
	total *= (1-y)

print '%6f' %(sum(total))