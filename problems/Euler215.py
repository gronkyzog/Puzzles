import itertools

def iscrack(X):
	xp = -1
	for x in X:
		if x == xp and x!=0:
			return True
		xp = x
	return False


nrows = 3
ncols = 9

blocks = [2,3]

start = tuple([0 for i in range(nrows)])

solutions = {start:1}

total = 0
for i in range(200):
	temp = {}
	for X,v in solutions.items():
		p = X.index(sorted(X)[0])
		for b in blocks:
			Y =list(X)
			Y[p]+=b
			Y = tuple(Y)
			if max(Y)==min(Y)==ncols:
				#print p,X,Y
				total+=v

			if max(Y) <= ncols and iscrack(Y)==False:
				if Y not in temp:
					temp[Y] = v
				else:
					temp[Y]+=v

	solutions = temp
	print i,len(solutions),sum(temp.values()),total,temp
	if len(temp)==0:
		break
