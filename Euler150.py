# start with triangles of depth 1
# sum two triangles below, they have an overlap, this is counted twice. remove it
# t(r,c,k) = S(r,c)+T(r+1,c,k-1) + T(r+1,c+1,k-1) - T(r+2,c+1,k-2)
# T(r,c,1) = S(r,c)
# T(r,c,0) = 0


import numpy
A = []
t=0
for k in range(1,500501):
	t = (615949*t + 797807) % 2**20
	A.append(int(t-2**19))
A.reverse()

S = numpy.zeros([1000,1000],dtype= numpy.long)
for s in range(0,1000):
	S[s,:s+1] = [A.pop() for i in range(s+1)]


TP = numpy.zeros([1001,1001],dtype= numpy.long)
T  = S

best = T.min()
for i in range(1,1000):
	# calculate trianges of depth i.
	# continue until 1 super triangle with all points
	# min at each level
	N =  S[:-1,:-1] + T[1:,:-1] + T[1:,1:] - TP[2:,1:-1]
	T,TP,S = N,T,S[:-1,:-1]
	best = min(best,T.min())
	print i,best










