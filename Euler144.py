import numpy

def normal(V):
	return V/(numpy.sum(V**2)**0.5)

def reflect(A,V,P):
	# takes a incident vector and reflects off an elipse with parameters A at positiob B
	# the incidedent vector is projected onto normal and tangent vectors
	# the reflected vector has the normal component reversed
	# finally the exit vector is projected back to the original cartesian coordinates
	N = normal(P/(A**2))
	T = normal(numpy.array([-N[1],N[0]]))
	M = numpy.array([N,T])
	W = numpy.dot(M,V)
	# reflect the normal component, keep tangent component the same
	return numpy.dot(M.T,[-W[0],W[1]])

def intersect(A,V,P):
	# assuming parametised line starts on a ellipse
	# fin the next position which the vector intercepts the ellipse
	# V is the direction vector, P is the initial position 
	# A is the parameters of the circle
	a = numpy.sum((V/A)**2)
	b = 2.*numpy.sum((P*V)/(A**2))
	s = -b/a
	return P + s*V

A =  numpy.array([5.,10.])
P0 = numpy.array((0.0,10.1))
P1 = numpy.array((1.4,-9.6))
#P = P1
V = normal(P1 - P0)

# start at P1 with original vector reflected
P = P1
V = reflect(A,V,P)
for i in range(1000):
	#print i,P,V,numpy.sum((P/A)**2)
	print '%d,%f,%f' %(i,P[0],P[1])
	if -0.01< P[0]< 0.01 and P[1] > 0:
		# hit top of the elipse. I forgot about the P[1]>0 at first.

		break
	P = intersect(A,V,P)
	V = reflect(A,V,P)

print i


