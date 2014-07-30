
def test():
	n = 10**7
	A = [0 for i in range(n+1)]
	A[0]=0
	A[1]=1
	for s in xrange(1,n):
		for k in xrange(2,n+1,s):
			A[k] +=1
		if s % 10000==0:
			print s

	return sum([1 for i in range(1,n) if A[i]== A[i+1]])

print test()