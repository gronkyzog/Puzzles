import numpy

def cycle(q,k):
	if k==1:
		for x in range(0,q):
			yield [x]
	else:
		for a in range(0,q):
			for x in cycle(q,k-1):
				output = [a]
				output.extend(x)
				yield output


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

n=6
P = primeseive(10**n)
dP = [extract_digits(p) for p in P]
dP = [p for p in dP if len(p)==n]

print 'Start Cycle'
for x in cycle(2,n):
	if x[-1] == 0:
		continue
	find = False
	#print x
	defmap = {}
	for p in dP:
		filtered_p = tuple([p[i] for i in range(0,n) if x[i]==1])
		excluded_p = tuple([p[i] for i in range(0,n) if x[i]!=1])
		if len(set(excluded_p))==1:
			if filtered_p not in defmap:
				defmap[filtered_p] = []
			defmap[filtered_p].append(build_number(p))

	for k,v in defmap.items():
		if len(v) >= 8:
			print x,k,v
			find = True
			break
	if find:
		break
			
								







