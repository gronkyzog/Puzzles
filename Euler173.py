def factor_pairs(n):
	output = [[] for i in range(n+1)]
	for s in range(2,n+1):
			for x,k in enumerate(range(2*s,n+1,s),start=2):
				if s < x:
					output[k].append((s,x))

	return output


A= factor_pairs(10**6)

B = [[((x[1]-x[0])/2,(x[0]+x[1])/2) for x in X if (x[0]+x[1]) % 2 ==0 and x[0] %2 ==0] for X in A]

print sum([len(b) for b in B])