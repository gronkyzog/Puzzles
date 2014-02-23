import numpy
def polyfit(X,Y):
	n= len(X)
	A = numpy.array([[x**i for i in range(n)] for x in X])
	B = numpy.linalg.solve(A,Y)
	return [int(round(b)) for b in B]

def polyfit2(X,Y):
	total = numpy.zeros([len(X)])
	for i,(z,y) in enumerate(zip(X,Y)):
		poly = numpy.array([1.])
		for j,x in enumerate(X):
			if i != j:
				poly = numpy.convolve(numpy.array([-x,1]),poly)
		f = eval(poly,z)
		poly = (poly*y)/f
		print x,poly,f,z
		total += poly
	print total
	return total



def eval(A,x):
	return sum([a*x**i for i,a in enumerate(A)])
		




def f(n):
	return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
	#return n**2 + 2*n + 3


X = [1,2,3]
Y = [1,4,9]
F = polyfit2(X,Y)

for x,y in zip(X,Y):
	print x,y,eval(F,x)


