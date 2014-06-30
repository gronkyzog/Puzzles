import itertools

n=20
q=10
maxsum = 9
window = 3

X = [x for x in itertools.product(range(q),repeat=window-1)]
mapper = {x:[y for y in X if sum(y)+x[0]<=maxsum and x[1]==y[0]] for x in X}
countmap = {x: (1 if sum(x)<= maxsum else 0) for x in X}

for i in range(3,n+1):
	temp = {x: sum([countmap[s] for s in mapper[x]]) for x in X}
	countmap = temp
	print i,sum([countmap[x] for x in X if x[0]!=0])

