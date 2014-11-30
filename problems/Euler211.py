import numpy

def is_perfect_square(x):
	rx = int(round(x**0.5))
	return rx**2 == x

n = 64*10**6

A = numpy.ones([n],dtype=long)
for k in xrange(2,n):
	if k% 100000 ==0:
		print k
	k2 = k**2
	A[k::k] += k2

print max(A)

total = 0
for i,a in enumerate(A):
	if is_perfect_square(a):
		total += i
		print i,a,total
print total

