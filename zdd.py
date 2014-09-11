# (-1,0,0) False
# (-1,1,1) True


#def S(k,U,X):
## to do.
## need to chang the construction of the head
## ZDD[0] points to the head's key. its always an integer. < this ones works better.
## The alternative is that ZDD[0] is the head. when its merged upstream, each of the 2 zeros it needs to be corrected.

import itertools

TrueNode = tuple([-1,1,1])
FalseNode = tuple([-1,0,0])
TrueHash = hash(TrueNode)
FalseHash = hash(FalseNode)



def Symmetric(k,X,U,hashMap=None,ZDD=None):
	if hashMap == None:
		hashMap = {}
		ZDD = {}
		exportflag = True
	else:
		exportflag = False

	key = tuple([k,tuple(X),tuple(U)])

	if k==0 and len(U) == 0:
		val = TrueNode
		head = hash(val)
		hashMap[key] = head
		ZDD[head] = val
		ZDD[0] = head
		if exportflag:
			return ZDD
		else:
			return head

	elif k > len(X):
		val = FalseNode
		head = hash(val)
		hashMap[key] = head
		ZDD[head] = val
		ZDD[0] = head
		if exportflag:
			return ZDD
		else:
			return head



	elif (k!=0 and len(U) == 0) or k < 0:
		val = FalseNode
		head = hash(val)
		hashMap[key] = head
		ZDD[head] = val
		ZDD[0] = head

		if exportflag:
			return ZDD
		else:
			return head

	else:
		v = min(U)
		X0 = [u for u in X if u!=v]
		U0 = [u for u in U if u!=v]
		if key in hashMap:
			head = hashMap[key]
			ZDD[0] = head
			if exportflag:
				return ZDD
			else:
				return head
		else:
			if v in X:
				head0 = Symmetric(k,X0,U0,hashMap,ZDD)
				head1 = Symmetric(k-1,X0,U0,hashMap,ZDD)
				if head1 == hash(FalseNode):
					#print head1
					ZDD[0] = head0
					hashMap[key] = head0
					if exportflag:
						return ZDD
					else:
						return head0
				val = tuple([v,head0,head1])
				head = hash(val)
				hashMap[key] = head
				ZDD[head] = val
				ZDD[0] = head
				if exportflag:
					return ZDD
				else:
					return head
			else:
				head0 = Symmetric(k,X0,U0,hashMap,ZDD)	
				if head0 == hash(FalseNode):
				 	ZDD[0] = head0
				 	return head0

				val = tuple([v,head0,head0])
				head = hash(val)
				hashMap[key] = head
				ZDD[head] = val
				ZDD[0] = head
				if exportflag:
					return ZDD
				else:
					return head


def ZDDIntersect(F,G):
	ZDD = {}
	hashMap = {}
	fhash,ghash = F[0],G[0]
	def intersect(fhash,ghash):
		key = tuple([fhash,ghash])
		if key in hashMap:
			head = hashMap[key]
			return head

		else:
			f,g = F[fhash],G[ghash]
			v,w = f[0],g[0]
			fhash0,fhash1 = f[1],f[2]
			ghash0,ghash1 = g[1],g[2]

			if fhash == FalseHash or ghash == FalseHash:
				val = FalseNode
				head = FalseHash
				hashMap[key] = head
				ZDD[head] = val
				return head

			elif fhash == TrueHash and ghash == TrueHash:
				val = TrueNode
				head = TrueHash
				hashMap[key] = head
				ZDD[head] = val
				return head		

			elif fhash == TrueHash:
				head0 = intersect(fhash,ghash0)
				head1 = FalseHash
				val = tuple([w,head0,head1])
				head = hash(val)
				hashMap[key] = head
				ZDD[head] = val
				return head	


			elif ghash == TrueHash:
				head0 = intersect(fhash0,ghash)
				head1 = FalseHash
				val = tuple([v,head0,head1])
				head = hash(val)
				hashMap[key] = head
				ZDD[head] = val
				return head					

			else:
				if v == w:
					head0 = intersect(fhash0,ghash0)
					head1 = intersect(fhash1,ghash1)
					val = tuple([v,head0,head1])
					head = hash(val)
					hashMap[key] = head
					ZDD[head] = val
					return head		

				elif v < w:
					head0 = intersect(fhash0,ghash)
					head1 = intersect(fhash1,ghash)
					val = tuple([v,head0,head1])
					head = hash(val)
					hashMap[key] = head
					ZDD[head] = val
					return head		

				else:
					head0 = intersect(fhash,ghash0)
					head1 = intersect(fhash,ghash1)
					val = tuple([v,head0,head1])
					head = hash(val)
					hashMap[key] = head
					ZDD[head] = val
					return head	


				






	head = intersect(fhash,ghash)
	ZDD[0] = hash(head)
	return ZDD





def cycle(ZDD,row):
	if row ==0:
		node,low,hi = ZDD[ZDD[0]]
	else:
		node,low,hi = ZDD[row]
	if node ==-1:
		if low==1:
			yield []

	else:
		for x in cycle(ZDD,hi):
			# the current node is not included
			temp = [node]
			temp.extend(x)
			yield temp

		for x in cycle(ZDD,low):
			# the current node is included
			yield x

def  ZDDcountSolutions(ZDD):
		hashMap = {}
		headhash= ZDD[0]
		def nsoultions(headhash):
			head = ZDD[headhash]
			if headhash in hashMap:
				return hashMap[headhash]
			

			elif head == TrueNode:
				hashMap[headhash] = 1
				return 1
			elif head == FalseNode:
				hashMap[headhash] = 0
				return 0

			else:
				lo = head[1]
				hi = head[2]
				total = nsoultions(lo)+nsoultions(hi) 
				hashMap[headhash] = total
				return total
		return nsoultions(headhash)








ZDD1 = Symmetric(5,range(10),range(10))
ZDD2 = Symmetric(2,[2,3,5],[1,2,3,4,5])
ZDD3 = ZDDIntersect(ZDD1,ZDD2)



F1 = [tuple(x) for x in cycle(ZDD1,0)]
F2 = [tuple(x) for x in cycle(ZDD2,0)]
F3 = [tuple(x) for x in cycle(ZDD3,0)]

F4 = [x for x,y in F1,F2 if x==y]







# ZDD3 = ZDDIntersect(ZDD1,ZDD2)








































# # def buildZDD(F):
# # 	if len(F)==0:
# # 		val = tuple([-1,0,0])
# # 		head = hash(val)
# # 		return {head:val},head

# # 	elif len(F)==1 and len(F[0])==0:
# # 		val = tuple([-1,1,1])
# # 		head = hash(val)
# # 		return {head:val},head
# # 	else:
# # 		v = min([min(f) for f in [g for g in F if len(g)>0]])
# # 		F0 = [f for f in F if v not in f]
# # 		F1 = [[a for a in f if a!=v] for f in F if v in f]
# # 		Zdd0,head0 = buildZDD(F0)
# # 		Zdd1,head1 = buildZDD(F1)
		
# # 		val = tuple([v,head0,head1])
# # 		head = hash(val)
# # 		Zdd = {head:val}
# # 		Zdd.update(Zdd0)
# # 		Zdd.update(Zdd1)

		

# def Symmetric(k,X,U):
# 	if k==0 and len(U) == 0:
# 		val = tuple([-1,1,1])
# 		head = hash(val)
# 		return {0:head,head:val}

# 	elif (k!=0 and len(U) == 0) or k < 0:
# 		val = tuple([-1,0,0])
# 		head = hash(val)
# 		return {0:head,head:val}

# 	else:
# 		v = min(U)
# 		X0 = [u for u in X if u!=v]
# 		U0 = [u for u in U if u!=v]	
# 		if v in X:
# 			Zdd0 = Symmetric(k,X0,U0)
# 			Zdd1 = Symmetric(k-1,X0,U0)		
# 			val = tuple([v,Zdd0[0],Zdd1[0]])
# 			head = hash(val)
# 			Zdd = {head:val}
# 			Zdd.update(Zdd0)
# 			Zdd.update(Zdd1)
# 			Zdd[0] = head
# 			return Zdd
# 		else:
# 			Zdd0 = Symmetric(k,X0,U0)	
# 			val = tuple([v,Zdd0[0],Zdd0[0]])
# 			head = hash(val)
# 			Zdd = {head:val}
# 			Zdd.update(Zdd0)
# 			Zdd[0] = head
# 			return Zdd


# def pophead(ZDD):
# 	ZDD0 = dict(ZDD)
# 	ZDD1 = dict(ZDD)
# 	head = ZDD[0]

# 	v,lo,hi = ZDD[head]
	
# 	ZDD0.pop(head)
# 	ZDD1.pop(head)
# 	ZDD0[0] = hash(ZDD[lo])
# 	ZDD1[0] = hash(ZDD[hi])
# 	return ZDD0,ZDD1








# hashmap = {}


# def mergeAnd(F,G,k=0):
# 	key = tuple([F[0],G[0]])
# 	if key in hashmap:
# 		return hashmap[key]

# 	Zdd = {}
# 	headF = F[F[0]]
# 	headG = G[G[0]]
# 	v,w = headF[0],headG[0]

# 	if headF == tuple((-1,0,0)):
# 		hashmap[key] = F
# 		return F
# 	elif headF == tuple((-1,1,1)):
# 		hashmap[key] = G
# 		return G

# 	elif headG == tuple((-1,0,0)):
# 		hashmap[key] = G
# 		return G
# 	elif headF == tuple((-1,1,1)):
# 		hashmap[key] = F
# 		return F
# 	elif v==w:
# 		F0,F1= pophead(F)
# 		G0,G1= pophead(G)
# 		H0 = mergeAnd(F0,G0,k+1)
# 		H1 = mergeAnd(F1,G1,k+1)
# 		val = tuple([v,H0[0],H1[0]])
# 		head = hash(val)
# 		Zdd = {head:val}
# 		Zdd.update(H0)
# 		Zdd.update(H1)
# 		Zdd[0] = head
# 		hashmap[key] = Zdd
# 		return Zdd

# 	elif v<w:
# 		F0,F1= pophead(F)
# 		#H = mergeAnd(F0,G) for or
# 		H = mergeAnd(F,G,k)  # for and
# 		val = tuple([v,H[0],F1[0]])
# 		head = hash(val)
# 		Zdd = {head:val}
# 		Zdd.update(H)
# 		Zdd.update(F1)
# 		Zdd[0] = head
# 		hashmap[key] = Zdd
# 		return Zdd

# 	else:
# 		G0,G1= pophead(G)
# 		#H = mergeAnd(F0,G) for or
# 		H = mergeAnd(F,G)  # for and
# 		val = tuple([v,H[0],G1[0]])
# 		head = hash(val)
# 		Zdd = {head:val}
# 		Zdd.update(H)
# 		Zdd.update(G1)
# 		Zdd[0] = head
# 		hashmap[key] = Zdd
# 		return Zdd















# def cycle(ZDD,row):
# 	if row ==0:
# 		node,low,hi = ZDD[ZDD[0]]
# 	else:
# 		node,low,hi = ZDD[row]
# 	if node ==-1:
# 		if low==1:
# 			yield []

# 	else:
# 		for x in cycle(ZDD,low):
# 			# the current node is not included
# 			yield x
# 		for x in cycle(ZDD,hi):
# 			# the current node is included
# 			temp = [node]
# 			temp.extend(x)
# 			yield temp

# def dist(A,B):
# 	return len([1 for a,b in zip(A,B) if a==b])



# #A = [[0, (2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5)], [1, (3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8)], [1, (3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7)], [1, (4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6)], [1, (6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0)], [1, (6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0)], [1, (8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3)], [2, (2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8)], [2, (2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9)], [2, (2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7)], [2, (4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7)], [2, (5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2)], [2, (5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3)], [2, (6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8)], [3, (1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6)], [3, (1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9)], [3, (3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5)], [3, (4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3)], [3, (5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7)], [3, (7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7)], [3, (8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4)], [3, (9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3)]]
# A = [[0, (7, 0, 7, 9, 4)], [1, (1, 2, 5, 3, 1)], [1, (3, 4, 1, 0, 9)], [2, (3, 9, 4, 5, 8)], [2, (5, 1, 5, 4, 5)], [2, (9, 0, 3, 4, 2)]]

# n = len(A[0][1])
# print n

# U = range(n*10)
# k1 = A[0][0]
# k2 = A[1][0]
# k3 = A[2][0]

# v1 = A[0][1]
# v2 = A[1][1]
# v3 = A[2][1]

# X1 =  [i*10 + q for i,q in enumerate(v1)]
# X2 =  [i*10 + q for i,q in enumerate(v2)]
# X3 =  [i*10 + q for i,q in enumerate(v3)]

# ZDD1 = Symmetric(k1,X1,U)
# ZDD2 = Symmetric(k2,X2,U)
# ZDD3 = Symmetric(k3,X3,U)


# ZDD = mergeAnd(ZDD1,ZDD2)
# ZDD = mergeAnd(ZDD,ZDD3)


# for i in range(n):
# 	temp = Symmetric(1,[s + i*10 for s in range(10)],range(n*10))
# 	ZDD = mergeAnd(temp,ZDD)
# 	#print i,len(ZDD)



# for x in cycle(ZDD,0):




# # ZDD = None


# # # for v,x in A:
# # # 	X = [i*10 + q for i,q in enumerate(x)]
# # # 	temp = Symmetric(v,X,range(len(x)*10))

# # # 	if ZDD is None:
# # # 		ZDD = temp
# # # 	else:
# # # 		ZDD = mergeAnd(temp,ZDD)
# # # 	#print x,v,len(ZDD)




# # # print len(ZDD)
# # # for x in cycle(ZDD,0):
# # #  	print x






