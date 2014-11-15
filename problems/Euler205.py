import numpy
# f  and g are the moment generating functions for each dice, the totals go from (0,q-1) instead of (1,q)
#  combine the distriubutions f^9 and g^6  this gives a total.

qf = 4
qg = 6

nf = 9
ng = 6
threshold = 28

f = numpy.poly1d([1./qf for i in range(qf)])
g = numpy.poly1d([1./qg for i in range(qg)])


h = (f**nf)*(g**ng)
print '%1.7f' % sum(h.coeffs[threshold:])
