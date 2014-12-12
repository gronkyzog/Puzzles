import itertools
def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)+1))



def product(A):
	output = 1
	for a in A:
		output *= a
	return output
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


def factorise(P,n):
	A = [[] for i in range(0,n+1)]

	for p in P:
		k=0
		while  True:
			k +=1
			q = p**k
			if q > n:
				break

			[A[s].append(p) for s in range(q,n,q)]
	return A
			
def alldivisors(F):
	A = list(set(F))
	output = []

	for x in itertools.product(*[range(F.count(a)+1) for a in A]):
		z = product(f**s for f,s in zip(A,x))
		if z > 1:
			output.append(z)
	output.sort()
	return output 

def cycle(A,n):
	P = A[n]
	for p in P:
		r =n/p 
		if r ==1:
			yield set([p])
		else:
			for x in cycle(A,r):
				y = list(x)
				y.append(p)
				yield y


P = primesieve(10**5)
A = factorise(P,10**5)
D = [alldivisors(a) for a in A]

defmap = {}
#for i in range(2,13):


for i in range(2,10**5):
	if len(defmap) == 11999:
		print 'Full'
		break
	for x in cycle(D,i):
		if len(x)==1:
			continue
		s = sum(x)
		w = len(x) + i-s
		if w not in defmap and w <= 12000:
			defmap[w]=i
	

print sum(set(defmap.values()))

