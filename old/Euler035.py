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

def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]

def cycle_digit(x):
	dx = extract_digits(x)
	dy = [dx[-1]]
	dy.extend(dx[:-1])
	return build_number(dy)

def cycle_all(x):
	output = []
	n = len(extract_digits(x))
	y = x
	for i in range(n):
		y = cycle_digit(y)
		output.append(y)
	return output

def build_number(x):
	A = x[::-1]
	return sum([a*10**i for i,a in enumerate(A)])


P  = set(primeseive(1000000))

counter = 0
for p in P:
	A = cycle_all(p)
	B = [a for a in A if a in P]
	if len(A)==len(B):
		print p,A,[a in P for a in A]
		counter +=1
print counter


