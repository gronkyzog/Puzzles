def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]


def freq_digits(x):
	Z= extract_digits(x)
	return tuple([Z.count(i) for i in range(0,10)])


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


n = 10**7
rootn = int(n**0.5)
P = primeseive(2*rootn)
nP = len(P)
print 'generation complete %d' %nP
print 'Assuming solition is product of two primes'
min_score = 100
for i in range(1,nP):
	for j in range(i+1,nP):
		pi,pj = P[i],P[j]
		z = pi*pj
		if z > 10**7:
			continue
		phi= z*(1-1./pi)*(1-1./pj) 
		fp = freq_digits(phi)
		fi = freq_digits(z)
		score = z/phi
		if fp == fi:
			if score < min_score:
				print z,phi,score
				min_score = score



