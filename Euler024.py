import math

def f(A,x):
	output = []
	R = list(A)
	r = x
	for i in xrange(len(A)-1,0,-1):
		q = math.factorial(i)
		k,r = divmod(r,q)

		output.append(R.pop(k))

	output.append(R.pop())
	return output



A = [0,1,2,3,4,5,6,7,8,9]
x = 999999

print x,''.join([str(s) for s in f(A,x)])