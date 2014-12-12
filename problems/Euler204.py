from eulertools import primesieve


N = 10**9
Q = 100
P = primesieve(Q)

prev = set([1])
solution = [prev]
for i in range(1,100):

	new = set([a*p for p in P for a in prev if a*p <= N])
	print i,len(new)
	if len(new)==0:
		break
	solution.append(new)
	prev = new


solution = set.union(*solution)
print len(solution)