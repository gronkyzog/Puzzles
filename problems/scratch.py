def cycle(x):
	counter = 0
	z = x
	while z>1:
		if z%2 ==0:
			z = z/2
		else:
			z = 3*z + 1
		counter +=1
	return counter
n = 10
A = [0 for i in range(n)]

for x in range(2,n):
	seq = [x]
	z= x
	while  z >1:
		if z%2 ==0:
			z = z/2
		else:
			z = 3*z + 1

		seq.append(z)
		if z < n:
			if A[z]>=0:
				break
	#seq.reverse()
	for i,s in enumerate(seq,start=1):
		if s < n:
			A[s] = A[z]+i


for i,a in enumerate(A):
	print i,a,cycle(i)