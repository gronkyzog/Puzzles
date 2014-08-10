import eulertools 
import math




r = 105

primitivepoints = {}
for x in range(-r+1,r):
	for y in range(-r+1,r):
		if  x**2 +y**2 < r**2 and (x,y)!= (0,0):
			k = abs(eulertools.gcd(x,y))
			key = (x/k,y/k)
			if key not in primitivepoints:
				primitivepoints[key]=0
			primitivepoints[key]+=1


for v in primitivepoints.values():
	print v


