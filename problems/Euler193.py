import itertools
import eulertools
N = 2**25
nMax = N
P = eulertools.primeseive(N)
def testP3(P):
	counter =0
	p0 = nMax
	Q0 = 1
	for p1 in P:
		Q1 = p1*Q0
		if p1 >= p0 or Q1 > nMax:
			break		
		for p2 in P:
			Q2 = p2*Q1
			if p2 >= p1 or Q2 > nMax:
				break
			else:
				for p3 in P:
					Q3 = p3*Q2
					if p3 >= p2 or Q3 > nMax:
						break
					else:	
						counter +=1
	return counter

def cycle(Qold,pold,k):
	if k==1:
		for p in P:
			Q = p*Qold
			if p>= pold or Q > nMax:
				return
			else:
				yield Q

	else:
		for p in P:
			Q= p*Qold
			if p>= pold or Q > nMax:
				return
			else:
				for x in cycle(Q,p,k-1):
					yield x






print 'complete'
#print testP3(P)
print len([x for x in cycle(1,N,1)])
print len([x for x in cycle(1,N,2)])
print len([x for x in cycle(1,N,3)])
print len([x for x in cycle(1,N,4)])
print len([x for x in cycle(1,N,5)])
print len([x for x in cycle(1,N,6)])	
print len([x for x in cycle(1,N,7)])
print len([x for x in cycle(1,N,8)])