import itertools
def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

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


def factorise(x,P):
	output = []
	r = x
	if x ==1:
		return [(1,1)]
	for p in P:
		while r % p ==0:
			output.append(p)
			r = r/p
			if r==1:
				break
	if r > 1:
		output.append(r)
	A = list(set(output))
	A.sort()
	return  [(a,output.count(a)) for a in A]

def divisors(n,P):
	try:
		output = []
		if n ==1:
			return [1]
		F = factorise(n,P)
		X,W= zip(*F)
		for E in itertools.product(*[range(e+1) for e in W]):
			z = product([x**e for x,e in zip(X,E)])
			output.append(z)
		output.sort()
		return output
	except:
		raise Exception('%d' %n )
	

total = 0
P = primesieve(1000000)
for s in range(1,10):
	solutions = set()
	n = 10**s
	D = divisors(n,P)
	for x,y in itertools.combinations_with_replacement(D,2):
		z = x+y
		if gcd(x,y)==1:
			a,b = n*z/x,n*z/y
			#print counter,z,x,y,a,b,len(set(divisors(a,P)).intersection(divisors(b,P)))
			Z = (set(divisors(a,P)).intersection(divisors(b,P)))
			for z in Z:
				sol = [a/z,b/z]
				sol.sort()
				solutions.add(tuple(sol))

	total += len(solutions)
	print s,total


print total