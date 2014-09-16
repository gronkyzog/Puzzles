import itertools

def mod_cumsum(X,q):
	Y= []
	tot = 0
	for s in X:
		tot = (tot+s) % q
		Y.append(tot)
	return tuple(Y) 

def generate_sequence(n):
	# any row can be generated by the following rule.
	# pick any 3 colour for the left most triangle, the following must be restricted to two colours (1,2)
	# apply a cumulative sum mod 3 to get the next colour (cycle up 1 or 2 colours) 
	output = []
	Q = [range(3)]
	[Q.append(range(1,3)) for i in range(n-1)]
	for x in itertools.product(*Q):
		y = mod_cumsum(x,3)
		output.append(y)
	return output

def iscompatible(X,Y):
	for x,y in zip(X,Y):
		if x==y:
			return False
	return True



A = {(0,):1,(1,):1,(2,):1}



for s in range(3,17,2):
	Anew = {}
	temp = generate_sequence(s)
	tempMap = {}
	for y in temp:
		n = len(y) 
		ytop = tuple([y[i] for i in range(1,n,2)])
		ybottom = tuple([y[i] for i in range(0,n,2)])
		if ytop not in tempMap:
			tempMap[ytop] = []
		tempMap[ytop].append(ybottom)

	for x,v in A.items():
		for ytop,YBottom in tempMap.items():
			if iscompatible(x,ytop):
				for ybot in YBottom:
					if ybot not in Anew:
						Anew[ybot] = v
					else:
						Anew[ybot] += v
	A = Anew
	#print s,len(A),sum(A.values())

print sum(A.values())