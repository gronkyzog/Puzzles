import eulertools 


def det(a,b):
	return a[0]*b[1]-b[0]*a[1]

r = 10

primitivepoints = {}
for x in range(-r+1,r):
	for y in range(-r+1,r):
		if eulertools.gcd(x,y) in (-1,1) and x**2 +y**2 < r**2:
			primitivepoints[(x,y)]=len([1 for k in range(1,r+1) if k**2*(x**2 + y**2) < r**2])


total = 0
for v1,n1 in primitivepoints.items():
	if v1[0]>0:
		for v2,n2 in primitivepoints.items():
			if det(v1,v2)>0:
				for v3,n3 in primitivepoints.items():
					if v3[0]<0:
						if det(v1,v2) >0 and det(v2,v3)>0 and det(v3,v1)>0 and v1>v2>v3:
								total += n1*n2*n3
		print v1,total

print total*2


#v1[0]*v2[1] > v2[0]*v1[1]
#v2[0]*v3[1] > v3[0]*v2[1]
#v3[0]*v1[1] > v1[0]*v3[1]




