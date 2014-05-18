import numpy
n = 16

X = numpy.array([13, 0, 1, 0, 1, 0, 0, 0],dtype=numpy.long)
A = numpy.array([[13, 0, 0, 0, 0, 0, 0, 0],
	             [ 1,14, 0, 0, 0, 0, 0, 0],
	             [ 1, 0,14, 0, 0, 0, 0, 0],   
	             [ 0, 1, 1,15, 0, 0, 0, 0],   
	             [ 1, 0, 0, 0,14, 0, 0, 0],   
	             [ 0, 1, 0, 0, 1,15, 0, 0],   
	             [ 0, 0, 1, 0, 1, 0,15, 0],  
	             [ 0, 0, 0, 1, 0, 1, 1,16]])
total = 0
for i in range(2,n+1):
	X = numpy.dot(A,X)
	total += X[-1]

print total
print hex(total).upper()[2:-1]


