def cycle(x,y):
	for i in range(x):
		for j in range(y):
			yield (i,j)

def dot(A,B):
	return A[0]*B[0]+ A[1]*B[1]


counter = 0
n = 50

Points = [x for x in cycle(n+1,n+1)]
npoints = len(Points)
for i in range(1,npoints):
	for j in range(i+1,npoints):
		OA = Points[i]
		OB = Points[j]

		AB = (OB[0]-OA[0],OB[1]-OA[1])				
		if dot(OA,OB) ==0  or dot(OA,AB)==0 or dot(OB,AB) ==0:
			if OA[0]*OB[1] - OA[1]*OB[0] != 0:
				counter +=1
				#print counter,OA,OB


print counter




