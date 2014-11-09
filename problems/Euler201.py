import numpy


S = [i**2 for i in range(1,101)]
#S = [1,3,6,8,10,11]
N = sum(S)+1
K = 50

A = {0:numpy.zeros(N+1,dtype=int)}
A[0][0]=1
for i,s in enumerate(S,start=1):
	print i,s,len(A)
	B = {k:1*v for k,v in A.items()}
	for k,v in A.items():
		key = k+1
		if key>K:
			continue
		else:
			temp = numpy.zeros(N+1,dtype=int)
			temp[s:] = v[:-s]

			if key not in B:
				B[key]=temp
			else:
				B[key]+=temp

	A = {k:1*v for k,v in B.items()}
	


print sum([i for i,a in enumerate(A[K]) if a==1])

