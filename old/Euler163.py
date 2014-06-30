import numpy 
import itertools

def sign(p1,p2,p3):
  return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0]- p3[0]) * (p1[1] - p3[1]);


def PointInTriangle(pt,v1,v2, v3):
  b1 = (sign(pt, v1, v2) <= 0)
  b2 = (sign(pt, v2, v3) <= 0)
  b3 = (sign(pt, v3, v1) <= 0)
  return ((b1 == b2) and (b2 == b3))


def line_intersection(x,y):
	A = numpy.array([-x[1],y[1]]).T
	#if abs(numpy.linalg.det(A))<0.1:
	#	raise Exception('WTF') 
	v = x[0]-y[0]
 	s = numpy.linalg.solve(A,v)
 	return x[0]+s[0]*x[1]



n =36

w = 2.**(-0.5)

e = 0.0001
boundary = [numpy.array((0.-e,0.-e)),numpy.array((n+e,0.-e)),numpy.array((0.5*n,n*w+e))]



lines = [[0,numpy.array([0.5*s,0.]),numpy.array([0.,1.])] for s in range(1,2*n)]
lines.extend([[1,numpy.array([0.,s*w]),numpy.array([1.,0.])] for s in range(0,n)])

lines.extend([[2,numpy.array([s,0.]),numpy.array([0.5,w])] for s in range(0,n)])
lines.extend([[3,numpy.array([s,0.]),numpy.array([-0.5,w])] for s in range(1,n+1)])

lines.extend([[4,numpy.array([s,0.]),numpy.array([0.75,0.5*w])] for s in range(0,n)])
lines.extend([[4,numpy.array([0.5*s,s*w]),numpy.array([0.75,0.5*w])] for s in range(1,n)])


lines.extend([[5,numpy.array([s,0.]),numpy.array([-0.75,0.5*w])] for s in range(1,n+1)])
lines.extend([[5,numpy.array([n-0.5*s,s*w]),numpy.array([-0.75,0.5*w])] for s in range(1,n)])



I = len(lines)

leylines = {}
for i,j in itertools.combinations(range(I),2):
	a,b = lines[i],lines[j]
	if a[0]!= b[0]:
		point = line_intersection(a[1:],b[1:])
		if PointInTriangle(point,*boundary):
			pt = tuple([round(point[0],4),round(point[1],4)])
			if pt not in leylines:
				leylines[pt] = set()
			leylines[pt].update([i,j])






leylines2 = {i:v for i,(k,v) in enumerate(leylines.items())}
print len(leylines2)




network = {}
for i,j in itertools.combinations(leylines2.keys(),2):
	if len(leylines2[i].intersection(leylines2[j])) > 0:
		if i not in network:
			network[i] = set()
		network[i].add(j)

		if j not in network:
			network[j] = set()
		network[j].add(i)


counter = 0
for a,B in network.items():
	for b in B:
		if a < b:
			C = network[b]
			for c in C:
				if b<c: 
					if a in network[c]:
						if len(leylines2[a].intersection(leylines2[b]).intersection(leylines2[c])) ==0:
							counter +=1
	print a,counter
print counter


