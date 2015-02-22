from random import randint
from numpy  import average,std


N = 100
dist = N/2


def iterate(A):
	newA = [0. for i in range(dist+1)]
	

	newA[0] = (18./36)*A[0] + (8./36)*A[1] + (1./36)*A[2]
	newA[1] = (16./36)*A[0] + (19./36)*A[1] + (8./36)*A[2] + (1./36)*A[3]
	newA[2] = (2./36)*A[0] + (8./36)*A[1] + (18./36)*A[2] + (8./36)*A[3] + (1./36)*A[4]

	for s in range(3,dist-2):
		newA[s] = (18./36)*A[s] + (A[s+1]+A[s-1])*(8./36) + (A[s+2]+A[s-2])*(1./36)

	newA[dist-2] = (8./36)*A[dist-1] + (18./36)*A[dist-2] + (8./36)*A[dist-3] + (1./36)*A[dist-4] 
	newA[dist-1] = (19./36)*A[dist-1] + (8./36)*A[dist-2] + (1./36)*A[dist-3]
	newA[dist]   = (8./36)*A[dist-1] +  (1./36)*A[dist-2]  

	return newA





A = [0. for i in range(dist+1)]

A[0] = 1.

total =0
for i in xrange(1,10**5):
	A = iterate(A)
	total += i*A[-1]

print total

