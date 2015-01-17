import itertools

class point():
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return '('+str(self.x)+','+str(self.y)+','+str(self.z)+')'

class cuboid():
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.area = (b.x-a.x)*(b.y-a.y)*(b.z-a.z) 
	def __str__(self):
		return '('+str(self.a)+','+str(self.b)+')'

def collide(cuboid1,cuboid2):
	a =point(max(cuboid1.a.x,cuboid2.a.x),max(cuboid1.a.y,cuboid2.a.y),max(cuboid1.a.z,cuboid2.a.z))
	b =point(min(cuboid1.b.x,cuboid2.b.x),min(cuboid1.b.y,cuboid2.b.y),min(cuboid1.b.z,cuboid2.b.z))
	if a.x < b.x and a.y < b.y and a.z < b.z:
		return cuboid(a,b)
	else:
		return None
def collide_list(cuboids):
	intersection = None
	for c in cuboids:
		if intersection == None:
			intersection = c
		else:
			intersection = collide(intersection,c)
			if intersection == None:
				return None
	return intersection


def split(cuboids):
	minx = min([c.a.x for c in cuboids])
	maxx = max([c.b.x for c in cuboids])

	miny = min([c.a.y for c in cuboids])
	maxy = max([c.b.y for c in cuboids])

	minz = min([c.a.z for c in cuboids])
	maxz = max([c.b.z for c in cuboids])

	mpx = (minx+maxx)/2
	mpy = (miny+maxy)/2
	mpz = (minz+maxz)/2

	distx = maxx- minx 
	disty = maxy- miny
	distz = maxz- minz

	maxdist = max([distx,disty,distz])

	if distx == maxdist:
		cuboid1 = cuboid(point(minx,miny,minz),point(mpx,maxy,maxz))
		cuboid2 = cuboid(point(mpx,miny,minz),point(maxx,maxy,maxz))
	elif disty == maxdist:
		cuboid1 = cuboid(point(minx,miny,minz),point(maxx,mpy,maxz))
		cuboid2 = cuboid(point(minx,mpy,minz),point(maxx,maxy,maxz))
	else:
		cuboid1 = cuboid(point(minx,miny,minz),point(maxx,maxy,mpz))
		cuboid2 = cuboid(point(minx,miny,mpz),point(maxx,maxy,maxz))

	output1 = []
	output2 = []
	for c in cuboids:
		c1 = collide(c,cuboid1)
		c2 = collide(c,cuboid2)
		if c1 is not None:
			output1.append(c1)
		if c2 is not None:
			output2.append(c2)

	output = []
	if len(output1)>0:
		output.append(output1)
	if len(output2)>0:
		output.append(output2)


	return output



def lagged_fibonachi():
	data = [100003]
	def f():
		k = len(data)
		if k <= 55:
			x =( 100003 - 200003*k + 300007*k**3)% 1000000
			data.append(x)
			return x
		else:
			x = (data[-24] + data[-55]) % 1000000
			data.append(x)
			data.pop(0)
			return x
	while True:
		x = f()
		yield x

def generate_cubes(n):
	S = lagged_fibonachi()
	cuboids = []
	for i in range(n):
		x = S.next() % 10000
		y = S.next() % 10000
		z = S.next() % 10000
		dx  = 1+(S.next() % 399)
		dy  = 1+(S.next() % 399)
		dz  = 1+(S.next() % 399)
		pointa = point(x,y,z)
		pointb = point(x+dx,y+dy,z+dz)
		cuboids.append(cuboid(pointa,pointb))

	return cuboids 


def partition_cuboids():
	split_cuboids = [generate_cubes(50000)]
	for i in range(40):
		temp = []
		exitFlag  = True
		for c in split_cuboids:
			if len(c) > 10:
				exitFlag = False
				temp.extend(split(c))
			else:
				temp.append(c)
		split_cuboids = temp
		print i, len(split_cuboids)
		if exitFlag:
			break
	print 
	return split_cuboids

def test_tupples(cuboids):
	n = len(cuboids)
	total = 0
	for k in range(1,n+1):
		sgn = -(-1)**k
		for x in itertools.combinations(cuboids,k):
			c = collide_list(x)
			if c is not None:
				total += sgn*c.area
	return total

def test_tupples2(cuboids):
	pass

partitions = partition_cuboids()
print len(partitions)
total = 0
for i,c in enumerate(partitions):
	total +=test_tupples(c)
print total

print 328968937309