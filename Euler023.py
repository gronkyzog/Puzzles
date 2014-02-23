def cycle(A,n):
	if n==1:
		for a in A:
			yield [a]
	else:
		for a in A:
			B = [s for s in A if a!=s]
			for b in cycle(B,n-1):
				output = [a]
				output.extend(b)
				yield output


def  f(n):
	A  = [0 for i in range(0,n)]
	for i in xrange(1,n):
		for j in xrange(2*i,n,i):
			A[j] += i
	return A

A = [i for i,a in enumerate(f(30000)) if a>i]
print len(A)
B = [0 for i in range(0,30000)]
n = len(A)
for  i in range(0,n):
	for j in range(0,i+1):
		 z = A[i]+ A[j]  
		 if z >= 30000:
		 	break
		 else:
		 	B[z]=1

total = 0
for i,b in enumerate(B):
	if b==0:
		total += i
		print i,total


#print A[:10]