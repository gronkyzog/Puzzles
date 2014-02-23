import numpy
def f(N,K):
	output = numpy.zeros([N+1,K+1],dtype = numpy.int)
	output[:,0]=0
	output[0,:]= 1

	for n in range(1,N+1):
		for k in range(1,K+1):
			if n < k:
				output[n,k] = output[n,k-1]
			else:
				output[n,k] = output[n,k-1] + output[n-k,k]
	return output[N,K]



print f(100,99)