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

N = primitivepoints.values()
a = sum(N)/2
c = sum(n**2 for n in N)/2
b = (a**2 - c)/2


sol = sum([b*n-a*n**2 + n**3 for n in N])/3

print sol






