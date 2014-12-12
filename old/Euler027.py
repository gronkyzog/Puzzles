import numpy
def primesieve(n):
    # return all primes <= n
    A = numpy.zeros([n+1])
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]


P =set(primesieve(10000))

max_counter = 0
for a in range(-100,1000):
	for b in range(-100,1000):
		x = 0
		while True:
			f = x**2 +a*x + b
			if f not in P:
				break
			x+=1
		if x > max_counter:
			max_counter = x
			print x,a,b,a*b