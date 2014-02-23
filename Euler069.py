
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

def bulk_phi(A,n):
	output = [i for i in range(0,n+1)]
	for x in A:
		for i in  range(x,n,x):
			z = output[i]
			z = (z*(x-1))/x
			output[i] =z
	return output


def phi(x,F):
	total = x
	for a in F:
		total = (total*(a-1))/a
	return total

P = primeseive(10**6)
A = bulk_phi(P,10**6)

max_r = 0
for i in range(1,10**6):
	p = A[i]
	r = (1.*i)/p
	if r > max_r:
		max_r = r
		print i,p,r,A[i]
