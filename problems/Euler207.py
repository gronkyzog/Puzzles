from math import log


counter = 0
ratio = 0
for x in xrange(2,10**6):
	k = ((2*x -1)**2 - 1)/4
	t = log(x,2)


	if abs(round(t,1)-t) < 1e-10:
		counter +=1

	if counter*12345 < (x-1):
		print x-1,x,k,t,counter,(1.*counter)/(x-1)
		break
print k

