import numpy


def primeseive(n):
    # return all primes <= n
    A = [0 for i in range(0,n+1)]
    for i in range(4,n+1,2):
                A[i]=1

    for i in range(3,n+1,2):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i): 
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]


def f(N,K):
	primes = set(primeseive(K))
	output = numpy.zeros([N+1,K+1],dtype = numpy.int)
	output[:,0]=0
	output[0,:]= 1

	for n in range(1,N+1):
		for k in range(1,K+1):
			if n < k or k not in primes:
				output[n,k] = output[n,k-1]
			else:
				output[n,k] = output[n,k-1] + output[n-k,k]
	return output[N,K]



for i in range(0,200):
	n =f(i,i)
	if n >= 5000:
		print i,n
		break