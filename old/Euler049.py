import numpy
def primesieve(n):
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


def cycle(A,k):
	if k==1:
		for a in A:
			yield [a]
	else:
		for i,a in enumerate(A):
			B = [b for j,b in enumerate(A) if i != j]
			for x in cycle(B,k-1):
				output = [a]
				output.extend(x)
				yield output





A = primesieve(10000)
A = set([a for a in A if a > 1000])
group = []
while len(A)>0:
	a = A.pop()
	da= extract_digits(a)
	temp = [a]
	[temp.append(build_number(x)) for x in cycle(da,len(da)) if build_number(x) in A] 
	temp.sort()
	if len(temp)>=3:
		for x in cycle(temp,3):
			x.sort()
			if x[1]-x[0]==x[2]-x[1] and x[1]-x[0] > 0:
				group.append(x)
				break

for x in group:
	print x
