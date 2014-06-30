import numpy

def primeseive(n):
    # return all primes <= n
    A = numpy.zeros([n+1])
    for i in range(2,n+1):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i):
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]


def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


def build_number(x,q=10):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])




P = set(primeseive(10000000))
A = [2,3,5,7]
total = list(A)
for z in range(0,7):
	newsol = []
	for x in A:
		for i in range(0,10):
			y = x*10 + i
			if y in P:
				newsol.append(y)

	print newsol
	if len(newsol)>0:
		total.extend(newsol)
		A = list(newsol)
	else:
		break


sum_primes = 0
for x in total:
	dx = extract_digits(x)
	include = True
	for i in range(0,len(dx)-1):
		w = build_number(dx[1:])
		if w not in P:
			include = False
		dx = extract_digits(w)
	if include and x > 10:
		print x
		sum_primes += x

print sum_primes
		



