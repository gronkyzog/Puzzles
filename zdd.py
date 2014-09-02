# (-1,0,0) False
# (-1,1,1) True


#def S(k,U,X):

## to do.
## need to chang the construction of the head
## ZDD[0] points to the head's key. its always an integer. < this ones works better.
## The alternative is that ZDD[0] is the head. when its merged upstream, each of the 2 zeros it needs to be corrected.

import itertools


F = [f for f in itertools.combinations(range(10),4)]



# def buildZDD(F):
# 	if len(F)==0:
# 		val = tuple([-1,0,0])
# 		head = hash(val)
# 		return {head:val},head

# 	elif len(F)==1 and len(F[0])==0:
# 		val = tuple([-1,1,1])
# 		head = hash(val)
# 		return {head:val},head
# 	else:
# 		v = min([min(f) for f in [g for g in F if len(g)>0]])
# 		F0 = [f for f in F if v not in f]
# 		F1 = [[a for a in f if a!=v] for f in F if v in f]
# 		Zdd0,head0 = buildZDD(F0)
# 		Zdd1,head1 = buildZDD(F1)
		
# 		val = tuple([v,head0,head1])
# 		head = hash(val)
# 		Zdd = {head:val}
# 		Zdd.update(Zdd0)
# 		Zdd.update(Zdd1)

		

def Symmetric(k,X,U):
	if k==0 and len(U) == 0:
		val = tuple([-1,1,1])
		head = hash(val)
		return {0:head,head:val}

	elif (k!=0 and len(U) == 0) or k < 0:
		val = tuple([-1,0,0])
		head = hash(val)
		return {0:head,head:val}

	else:
		v = min(U)
		X0 = [u for u in X if u!=v]
		U0 = [u for u in U if u!=v]	
		if v in X:
			Zdd0 = Symmetric(k,X0,U0)
			Zdd1 = Symmetric(k-1,X0,U0)		
			val = tuple([v,Zdd0[0],Zdd1[0]])
			head = hash(val)
			Zdd = {head:val}
			Zdd.update(Zdd0)
			Zdd.update(Zdd1)
			Zdd[0] = head
			return Zdd
		else:
			Zdd0 = Symmetric(k,X0,U0)	
			val = tuple([v,Zdd0[0],Zdd0[0]])
			head = hash(val)
			Zdd = {head:val}
			Zdd.update(Zdd0)
			Zdd[0] = head
			return Zdd


def pophead(ZDD):
	ZDD0 = dict(ZDD)
	ZDD1 = dict(ZDD)
	head = ZDD[0]

	v,lo,hi = ZDD[head]
	
	ZDD0.pop(head)
	ZDD1.pop(head)
	ZDD0[0] = hash(ZDD[lo])
	ZDD1[0] = hash(ZDD[hi])
	return ZDD0,ZDD1











def mergeAnd(F,G):
	print 'Hello',len(F),len(G)
	Zdd = {}
	headF = F[F[0]]
	headG = G[G[0]]
	v,w = headF[0],headG[0]
	if v==w:
		F0,F1= pophead(F)
		G0,G1= pophead(G)
		H0 = mergeAnd(F0,G0)
		H1 = mergeAnd(F1,G1)
		val = tuple([v,H0[0],H1[0]])
		head = hash(val)
		Zdd = {head:val}
		Zdd.update(H0)
		Zdd.update(H1)
		Zdd[0] = head
		return Zdd

	elif v<w:
		F0,F1= pophead(F)
		#H = mergeAnd(F0,G) for or
		H = mergeAnd(F,G)  # for and
		val = tuple([v,H[0],F1[0]])
		head = hash(val)
		Zdd = {head:val}
		Zdd.update(H)
		Zdd.update(F1)
		Zdd[0] = head
		return Zdd

	else:
		G0,G1= pophead(G)
		#H = mergeAnd(F0,G) for or
		H = mergeAnd(F,G)  # for and
		val = tuple([v,H[0],G1[0]])
		head = hash(val)
		Zdd = {head:val}
		Zdd.update(H)
		Zdd.update(G1)
		Zdd[0] = head
		return Zdd


		














def cycle(ZDD,row):
	if row ==0:
		node,low,hi = ZDD[ZDD[0]]
	else:
		node,low,hi = ZDD[row]
	if node ==-1:
		if low==1:
			yield []

	else:
		for x in cycle(ZDD,low):
			# the current node is not included
			yield x
		for x in cycle(ZDD,hi):
			# the current node is included
			temp = [node]
			temp.extend(x)
			yield temp


ZDD1 = Symmetric(3,[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8,9,10])
ZDD2 = Symmetric(3,[1,2,3],[1,2,3,4,5,6,7,8,9,10])


ZDD3 = mergeAnd(ZDD1,ZDD2)
for x in cycle(ZDD1,0):
	print x



