def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def isPerfectSquare(x):
	rx = int(round(x**0.5))
	if (rx**2 - x) ==0:
		return True
	return False

maxsize = 120000
output = set()
for a in xrange(1,maxsize):
	print a
	for b in xrange(1,a):
		r = a**2 - 3*b**2
		s = 2*a*b
		if r < 0:
			break
		t = a**2 + 3*b**2
		#if t > 2*maxsize:
		#	break

		if t%2 ==0 and r%2 ==0:
			x0 = r/2 - a*b
			y0 = s
			z0 = t/2
			w =gcd(gcd(x0,y0),z0)
			if x0 > maxsize or y0>maxsize or z0 > maxsize:
				break
			x0,y0,z0 = x0/w,y0/w,z0/w
			for k in xrange(1,maxsize):
				x,y,z = k*x0,k*y0,k*z0
				if x+y > maxsize:
					break
				
				if x>0 and y>0:
					output.add((x,y,z))
					output.add((y,x,z))
			#print x,y,z,len(output)

print 'Generation Complete %d' % len(output)
mapper = {}
for x in output:
	if x[0] not in mapper:
		mapper[x[0]] = []
	mapper[x[0]].append(x[1])

for k,v in mapper.items():
	v = set(v)
print 'Mapper Complete %d' % len(mapper)

total = set()
for x,Y in mapper.items():
	for y in Y:
		Z = mapper[y]
		for z in Z:
			W = mapper[z]
			if x in W:
				temp = x+y+z
				if temp <= maxsize:
					print x,y,z,temp
					total.add(temp)


for x in total:
 	print x
print sum(total)


# counter = 0
# for x in range(1,maxsize):
# 	print x,counter
# 	for y in range(1,x+1):
# 		z2 = x**2 + y**2 + x*y
# 		if isPerfectSquare(z2):
# 			counter +=1
# 			z = int(round(z2**0.5))
# 			if (x,y,z) not in output:
# 				print x,y,z
# 				raise Exception('WTF')