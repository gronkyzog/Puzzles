import itertools

def powerset(iterable):
	s = list(iterable)
	return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(0,len(s)+1))

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


def lcm(a,b):
	return a*b/gcd(a,b)

def lcmarray(A):
	output = 1
	for a in A:
		output = lcm(output,a)
	return output

def generate_combinations(A,q,n):
	keys = A.keys()
	output = []
	base = [None for i in range(n+1)]
	for k in A.keys():
		base[k]=0

	for X in powerset(A):
		val = sum([A[x] for x in X]) % q
		if val ==0:
			temp = list(base)
			for k in  X:
				temp[k]= 1
			output.append(temp)

	return output


def merge_solitions(A,B):
	output = []
	n = len(A[0])
	for a in A:
		for b in B:
			c = [None for i in xrange(n)]
			insertflag = True
			for k in xrange(n):
				if a[k] is None:
					c[k] = b[k]
				elif b[k] is None:
					c[k] = a[k]
				elif a[k]==b[k]:
					c[k]= a[k]
				else:
					insertflag = False
			if insertflag:
				output.append(tuple(c))
	return list(set(output))

def generate_solutions(A,signature,target):
	I = [i for i,s in enumerate(signature) if s is None]
	J = [i for i,s in enumerate(signature) if s ==1]
	n = len(I)
	#print A
	output = []
	for Z in powerset(I):
		temp = sum([F/(A[j]**2) for j in J]) + sum([F/(A[z]**2) for z in Z])
		#print temp,target
		if temp == target:
			sol = [A[j] for j in J]
			sol.extend([A[z] for z in Z])
			sol.sort()
			output.append(sol)

	return output





n = 80
A = [i for i in range(2,n+1)]
F =  lcmarray(A)**2
B = {a: F/a**2 for a in A}

print F

A = [i for i in range(2,n+1)]
for i in range(10):
 	print i,len(A),A
 	AL = list(A)
 	for a in AL:
 		C = {b : int(B[b] % (a**2)) for b in A if B[b] % (a**2) != 0}
 		D =  generate_combinations(C,a**2,n)
 		if len(D)==1:
 			for k in C.keys():
 				A.remove(k)

#C = {b : int(B[b] % (2**2)) for b in A if B[b] % (2**2) != 0}
sol = [[ None if a in A else 0 for a in range(n+1)]]
sol[0][:4] = [0,0,1,1]
for a in A:
	C = {b : int(B[b] % (a**2)) for b in A if B[b] % (a**2) != 0}
	D =  generate_combinations(C,a**2,n)
	if sol is None:
		sol = D
	else:
		sol = merge_solitions(sol,D)
	#print a,len(sol)
#print A
counter = 0
print len(sol)
for i,x in enumerate(sol):
	print x
for i,x in enumerate(sol):

	temp =generate_solutions([s for s in xrange(n+1)],x,F/2)
	if len(temp)>0:
		counter += len(temp)
		print counter,temp
	
print counter

# A.remove(2)
# lA = len(A)
# counter = 0
# for x in itertools.product(xrange(2),repeat=(len(A))):
# 	if sum([x[i]*F/(A[i]**2) for i in xrange(lA)])== F/4:
# 		sol = [A[i] for i in xrange(lA) if x[i]==1]
# 		counter +=1
# 		print counter,sol
# #