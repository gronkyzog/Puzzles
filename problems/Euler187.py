import eulertools
N = 10**8

P = eulertools.primeseive(N)
counter = 0
print 'Go'
for p1 in P:
	for p2 in P:
		if p2 > p1:
			break
		q = p1*p2
		if q > N:
			break

		counter +=1

print counter
print 23378
print 17427258
