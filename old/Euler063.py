import math
counter = 0
for p in range(1,1000):
	for n in range(1,1000):
		x = p**n
		z = len(str(x))
		if z == n:
			counter +=1
			print counter,p,n,x
		if z > n:
			break
		