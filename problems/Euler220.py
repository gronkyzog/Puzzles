
import numpy
def position2(input_string):
	A = numpy.identity(4,numpy.int)
	F = numpy.array([[1,0,0,0],[0,1,0,0],[1,0,1,0],[0,1,0,1]])
	L = numpy.array([[0,1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,1]])
	R = numpy.array([[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])

	for i,s in enumerate(input_string):
		if s == 'F':
			A = numpy.dot(F,A)
		elif s == 'L':
			A = numpy.dot(L,A)
		elif s == 'R':
			A = numpy.dot(R,A)
	return A

def position(input,v0,p0,display=False):
	# direction position
	v = v0
	p = p0
	for i,s in enumerate(input):
		if s == 'F':
			p = [p[0]+v[0],p[1]+v[1]]
		elif s == 'L':
			v = [-v[1],v[0]]

		elif s == 'R':
			v = [v[1],-v[0]]
		if display and s == 'F':
			print '%d,%s,%d,%d,%d,%d' % (i,s,v[0],v[1],p[0],p[1])


	return v,p
aMap = 'cRdFR'
bMap = 'LFcLd'


D = 'Fa'
v0 = [0,1]
p0 = [0,0]
for i in range(1,10):
	D = D.replace('a',aMap).replace('b',bMap).replace('c','a').replace('d','b')
	P = position(D,v0,p0)
	A = position2(D)
	print numpy.dot(A,[0,1,0,0]),P


# D = 'Fa'
# v0 = [1,0]
# p0 = [0,0]

# for i in range(1,11):
# 	D = D.replace('a',aMap).replace('b',bMap).replace('c','a').replace('d','b')
# 	v,p = position(D,v0,p0)
# 	print  '%d,%d,%d,%d,%d' % (i,v[0],v[1],p[0],p[1])


	# Dprev  = D
	# v,p = position(D)
	# Aprev = Dprev.replace('a','').replace('b','')
	# A     = D.replace('a','').replace('b','')
	# print i,A == Aprev + 'RL'+Aprev
	# print 4*' '+A
	# print 4*' '+Aprev + 'R'+Aprev[::-1] + 'R'



# position(D,True)