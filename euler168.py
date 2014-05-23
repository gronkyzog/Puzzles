



for k in range(1,10):
	print k
	for x in xrange(10**k,10**(k+1)):
		q,r = divmod(x,10)
		y = q + r*10**k 
		q,r = divmod(y,x)
		if r ==0 and x != y:
			print '%d,%d,%d' % (x,y,q)
