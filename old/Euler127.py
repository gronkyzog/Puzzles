def primesieve(n):
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


def radicals(n):
    P = primesieve(n)
    output = [1 for i in range(0,n+1)]
    for p in P:
        for s in range(p,n+1,p):
            output[s] *= p
    return output

def product(A):
	product = 1
	for a in A:
		product *= a
	return product

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


maxsize = 120000
R = radicals(maxsize)


C = [(r,x) for x,r in enumerate(R)]
C.sort()




total = 0

for c,r in enumerate(R):
	if 2*r >= c:
		continue
	for a in range(1,c/2):
		b = c-a
		if R[a]*R[b]*R[c] < c:
			if gcd(a,b)==1:
				total += c
				print c,a,b,total,R[a],R[b],R[c]

print total