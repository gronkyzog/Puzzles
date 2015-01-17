from numpy import product

def primesieve(n):
    # return all primes <= n
    A = [0 for i in range(0,n+1)]
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]

def FactorCount(X):
		# calculates all combinations from a list of factors witch may contain duplicates
		# every product from the factor base can be written as powers a_i^(p_i) where p_i in [0,count(a_i)+1] 
		# the product over the exponent range gives the total count
		S = set(X)
		return product([(X.count(s)+1) for s in S])
		

def factor_over_base(P,x):
	output = []
	for p in P:
		while x % p ==0:
			output.append(p)
			x = x/p

	return output

 

P = primesieve(8751)  #  set this to a large number then rebalance to root the minimum value 


maxfactors = 0
for i in range(1,1000000):
	x = i*(i+1)/2
	A = factor_over_base(P,x)
	if len(A) > 9:
		nfactors = FactorCount(A)
		if nfactors > 500:
			print i,x,nfactors,A
			break
	


