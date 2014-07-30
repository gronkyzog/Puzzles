import eulertools 


def PointInTriangle(v1,v2,v3):
	s = (p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py);
	t = (p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py);

r = 2

primitivepoints = {}
for x in range(-r+1,r):
	for y in range(-r+1,r):
		if eulertools.gcd(x,y) in (-1,1) and x**2 +y**2 < r**2:
			primitivepoints[(x,y)]=len([1 for k in range(1,r+1) if k**2*(x**2 + y**2) < r**2])


total = 0
for v1,n1 in primitivepoints.items():
	for v2,n2 in primitivepoints.items():
		for v3,n3 in primitivepoints.items():
			if v1 < v2 < v3:
				if PointInTriangle(v1,v2,v3):
					print v1,v2,v2,n1*n2*n3
					total += n1*n2*n3

print total


# for k,v in primitivepoints.items():
# 	print k,v
