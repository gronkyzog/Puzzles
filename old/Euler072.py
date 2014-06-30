
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
		for i in  range(x,n+1,x):
			z = output[i]
			z = (z*(x-1))/x
			output[i] =z
	return output

P = primeseive(10**6)
A = bulk_phi(P,10**6)
print sum(A[2:])










