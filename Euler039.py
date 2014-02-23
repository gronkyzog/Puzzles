import numpy

A = [(a,b,int((a**2 + b**2)**0.5)) for a in range(1,500) for b in range(a,500)]
B = [a for a in A if a[0]**2 + a[1]**2 == a[2]**2 and a[0]+ a[1]+a[2] <= 1000]
print len(B)
C = [sum(b) for b in B]
D = [C.count(i) for i in range(0,1000)]
I = numpy.argsort(D)
print I[-1]
for a in B:
	if sum(a) == I[-1]:
		print a,sum(a)
