import csv
import math
import numpy

def normal(x):
	k = (x[0]**2 + x[1]**2)*0.5
	return (x[0]/k,x[1]/k)

def proj(A,B):
	# projection of A in direction of B
	return numpy.dot(A,normal(B))

def norm(x):
	return (x[0]**2 + x[1]**2)*0.5

csvreader = csv.reader(open('Euler102.txt','rb'),delimiter = ',',quotechar = '"')

data = []
for row in csvreader:
	 introw = [float(x) for x in row]
	 data.append([(introw[0],introw[1]),(introw[2],introw[3]),(introw[4],introw[5])])


counter = 0
for z in data:
	A = numpy.array(z[0])
	B = numpy.array(z[1])
	C = numpy.array(z[2])
	P = -A
	X = B - A
	Y = C - A
	lX = norm(X)
	lY = norm(Y)
	px,py = proj(P,X),proj(P,Y)
	if 0 < px < lX and 0 < py < lY:
		counter +=1 
		print z,counter



