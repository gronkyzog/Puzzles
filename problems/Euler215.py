
def not_cracked(X,xmax):
	xp = -1
	for x in X:
		if x==xp and x!=0 and x < xmax:
			return False
		xp = x
	return True

nrows = 10
ncols = 32


solution = {tuple([0 for i in range(nrows)]):1}

blocks = [2,3]

total = 0
for i in range(1000):
	temp = {}
	for X,v in solution.items():
		p = list(X).index(min(X))
		for b in blocks:
			Y = list(X)
			Y[p]+=b
			Y = tuple(Y)
			if max(Y)==min(Y) == ncols:
				total+=v
			elif not_cracked(Y,ncols) and  max(Y) <= ncols:
				w = temp.setdefault(Y,0)
				temp[Y] = w+v
	solution = temp
	print i,len(solution),total
	if len(solution)==0:
		break
print total

