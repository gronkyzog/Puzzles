import itertools 

S = [i for i in range(0,10)]


D = [[(0,1)],
	 [(0,4)],
	 [(0,6),(0,9)],
	 [(1,6),(1,9)],
	 [(2,5)],
	 [(3,6),(3,9)],
	 [(4,6),(4,9)],
	 [(6,4),(9,4)],
	 [(8,1)]
	 ]



sol = set()
for X in itertools.combinations(S,6):
  	for Y in itertools.combinations(S,6):
  		if Y < X:
  			continue
  			
  		include = True
  		for A in D:
  			matchflag = False
  			for a,b in A:
  				if (a in X and b in Y) or (a in Y and b in X):
  					matchflag = True
  			if matchflag == False:
  				include = False
  				break
  		
  		if include and X <= Y:
  			#print X,Y
  			sol.add((X,Y))

print len(sol)



