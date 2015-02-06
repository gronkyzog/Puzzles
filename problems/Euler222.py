import random



def f(K,R):
	rp = R[0]
	total = rp
	for r in R[1:]:
		total +=(-K*(K-2*r-2*rp))**0.5
		rp = r
	total += R[-1]
	return total


R = [r for r in range(30,51)]

minsol = 10**9
for counter in range(100):
	random.shuffle(R)
	n = len(R)
	K = 100
	for s in xrange(10**4):
		exitflag = True
		for i in xrange(n):
			for j in xrange(n):
				X = list(R)
				X[i] = R[j]
				X[j] = R[i]
				if f(K,X) < f(K,R):
					R = list(X)
					#print i,j,R,f(K,X)
					exitflag = False
		if exitflag:
			break

	sol = int(round(f(K,R)*1000,0))
	if sol < minsol:
		if R[0] > R[-1]:
			R = R[::-1]
		minsol = sol
		print counter,sol,R

print minsol