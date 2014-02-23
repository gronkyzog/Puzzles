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

def Factorize(P):
	pmax = max(P)
	output = [[] for i in range(pmax+1)]
	for p in P:
		k=1
		q = p**k
		while q <= pmax:
			for s in range(q,pmax+1,q):
				output[s].append(p)
			k +=1
			q = q*p
	return output


nmax = 10**5
P=primeseive(nmax)
F = Factorize(P)

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def cycle(x):
	q = 1
	k=1
	while True:
		q = (10*q + 1) %x
		k +=1
		if q ==0:
			return k 

counter = 0
total = 0
for x,F in enumerate(F):
	if gcd(x,10)==1:
		k = cycle(x)
		if ((x-1) % k)==0 and len(F)>1:
			counter +=1
			total += x
			print counter,total,x,k,F
			if counter ==25:
				break
print total

		



