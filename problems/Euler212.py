import itertools

def collide(a,b):
	a1,a2 = a[0],a[1]
	b1,b2 = b[0],b[1]
	c1 = (max(a1[0],b1[0]),max(a1[1],b1[1]),max(a1[2],b1[2]))
	c2 = (min(a2[0],b2[0]),min(a2[1],b2[1]),min(a2[2],b2[2]))
	if c1[0] < c2[0] and c1[1] < c2[1] and c1[2] < c2[2]:
		return (c1,c2)
	else:
		return None


def area(p):
	p1,p2 = p[0],p[1]
	return (p2[0]-p1[0])*(p2[1]-p1[1])*(p2[2]-p1[2])


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

def generate_cubes():
	S = lagged_fibonachi()
	cuboids = []
	for i in range(50000):
		x = S.next() % 10000
		y = S.next() % 10000
		z = S.next() % 10000
		dx  = 1+(S.next() % 399)
		dy  = 1+(S.next() % 399)
		dz  = 1+(S.next() % 399)
		cuboids.append(((x,y,z),(x+dx,y+dy,z+dz)))
	return cuboids

def split_cuboids(cuboids,axis):
	minx = min([x[0][0] for x in cuboids])
	maxx = max([x[1][0] for x in cuboids])

	miny = min([x[0][1] for x in cuboids])
	maxy = max([x[1][1] for x in cuboids])

	minz = min([x[0][2] for x in cuboids])
	maxz = max([x[1][2] for x in cuboids])
	distx = maxx-minx
	disty = maxy-miny
	distz = maxz-minz
	maxdist = max([distx,disty,distz])

	if axis==0:
		mp = minx + distx/2
		cubeoid1 = (minx,miny,minz),(minx+mp,maxy,maxz)
		cubeoid2 = (minx+mp,miny,minz),(maxx,maxy,maxz)
	elif axis==1: 
		mp = miny + disty/2
		cubeoid1 = (minx,miny,minz),(maxx,miny+mp,maxz)
		cubeoid2 = (minx,miny+mp,minz),(maxx,maxy,maxz)
	else:
		mp = minz + distz/2
		cubeoid1 = (minx,miny,minz),(maxx,maxy,minz+mp)
		cubeoid2 = (minx,miny,minz+mp),(maxx,maxy,maxz)


	output1 = []
	output2 = []
	for c in cuboids:
		c1= collide(c,cubeoid1)
		c2= collide(c,cubeoid2)

		if c1 is None and c2 is None:
			raise Exception('No Blocks')
		
		if c1 is not None:
			output1.append(c1)

		if c2 is not None:
			output2.append(c2)
	if len(output1)>0 and len(output2)>0:
		return [output1,output2]
	elif len(output1)>0:
		return [output1]
	else:
		return [output2]


def run():
	split_list =[generate_cubes()]
	for i in range(9):
		print i,len(split_list),max([len(s) for s in split_list]),sum([sum([area(s) for s in cuboids]) for cuboids in split_list])
		temp =[]
		ExitFlag = True
		for c in split_list:
			if len(c)==0:
				continue
			if len(c) < 2:
				temp.append(c)
			else:
				ExitFlag = False
				temp.extend(split_cuboids(c,i%3))
		split_list = temp
		if ExitFlag:
			break

	print len(split_list)

	cuboids = split_list[-1]
	print cuboids

run()



