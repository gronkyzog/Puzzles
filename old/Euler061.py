def cycle_permutation(A):
	if len(A)==1:
		yield [A[0]]

	else:
		for x in A:
			B = [a for a in A if a != x]
			for Z in cycle_permutation(B):
				output = [x]
				output.extend(Z)
				yield output





def cycle(A,k,lag,head=None,tail=None):
	if k ==1:
		B = [x for x in A[0] if tuple(x[-lag:])== tuple(head) and tuple(x[:lag]) == tuple(tail)]
		#print k,len(B),head,tail
		for x in B:
			yield [x]
	elif head==None and tail == None:
		for x in A[0]:		
			head = tuple(x[:lag])
			tail = tuple(x[-lag:])
			for Z in cycle(A[1:],k-1,lag,head,tail):
				output = [x]
				output.extend(Z)
				yield output

	else:
		if len(A[0]) > 0:
			B = [x for x in A[0] if  tuple(x[-lag:]) == tuple(head)]
			for x in B:
				head = tuple(x[:lag])
				for Z in cycle(A[1:],k-1,lag,head,tail):
					output = [x]
					output.extend(Z)
					yield output





def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]


def build_number(x,q=10):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])


def P(k,n):
	if k==3:
		return  n*(n+1)/2
	elif k==4:
		return n*n
	elif k==5:
		return  n*(3*n-1)/2
	elif k==6:
		return n*(2*n-1)
	elif k==7:
		return n*(5*n -3)/2
	elif k==8:
		return n*(3*n-2)
	else:
		raise


def run_me(A):
	for Z in cycle_permutation([0,1,2,3,4,5]):
			B = [A[z] for z in Z]
			for x in cycle(B,6,2):
				x.sort()
				print Z,x,sum([build_number(s) for s in x])
				return sum([build_number(s) for s in x])




A=  [[extract_digits(P(k,n)) for n in range(0,10000)  if P(k,n)>=1000 and  P(k,n) < 10000] for k in range(3,9)]


print run_me(A)	


# lag = 2
# for x in A[0]:
# 	key0 = tuple([x[0],x[1]])
# 	A1F = [a for a in A[1] if tuple([a[2],a[3]]) == key0 ]
# 	for y in A1F:
# 		key1 = tuple([y[0],y[1]])
# 		A2F = [a for a in A[2] if tuple([a[2],a[3]]) == key1 and  tuple([a[0],a[1]]) == tuple([x[2],x[3]])]
# 		for z in A2F:
# 			print x,y,z
