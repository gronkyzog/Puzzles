import itertools 

# def powerset(iterable,minsize=0):
#     s = list(iterable)
#     return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(minsize,len(s)+1))


def test_set(A):
	n = len(A)
	pos_map = {}
	for i in range(1,n+1):
		pos_map[i]= {}
		for x in itertools.combinations(A,i):
			sx = sum(x)
			if sx in pos_map[i]:
				return False
			else:
				pos_map[i][sx] = x
	
	for i in range(1,n):
		if max(pos_map[i].keys()) >= min(pos_map[i+1].keys()):
			return False

	return True


A = [20, 31, 38, 39, 40, 42, 45]
print test_set(A),sum(A)

B = [b for b in range(20,50)]

minsum = sum(A)
for X in itertools.combinations(B,7):
	if test_set(X):
		sx = sum(X)
		print sx,X,''.join([str(x) for x in X])
		if sx < minsum:
			minsum = sx




#X[i] < x[i+1]

#x[1]+x[2] > x[n]
#x[1]+x[2]+ x[3] > x[n-1] + x[n]
#x[1]+x[3] != x[2]+x[4]