# (-1,0,0) False
# (-1,1,1) True


#def S(k,U,X):
## to do.
## need to chang the construction of the head
## ZDD[0] points to the head's key. its always an integer. < this ones works better.
## The alternative is that ZDD[0] is the head. when its merged upstream, each of the 2 zeros it needs to be corrected.
import random
import itertools
import hashlib 

hashTable = {}
def hash2(x):
	return hashlib.sha224(str(x)).hexdigest()
	# if x in hashTable:
	# 	return hashTable[x]
	# else:
	# 	h = len(hashTable)+1
	# 	hashTable[x] = h
	# 	return h

	


TrueNode = tuple([-1,1,1])
FalseNode = tuple([-1,0,0])
TrueHash = hash2(TrueNode)
FalseHash = hash2(FalseNode)




def buildZDD(F):
	if len(F)==0:
		val = FalseNode
		head = hash2(val)
		return {0:head,head:val}
	elif len(F)==1 and tuple([]) in F:
		val = TrueNode
		head = hash2(val)
		return {0:head,head:val}
	else:
		V = [min(f) for f in [g for g in F if len(g)>0]]
		v = min(V)
		F0 = set([f for f in F if v not in f])
		F1 = set([tuple([w for w in f if w!=v]) for f in F if v in f])

		Zdd0 = buildZDD(F0)
		Zdd1 = buildZDD(F1)
		head0 = Zdd0[0]
		head1 = Zdd1[0]
		val = tuple([v,head0,head1])
		head = hash2(val)
		Zdd = {head:val}
		Zdd.update(Zdd0)
		Zdd.update(Zdd1)
		Zdd[0] = head
		return Zdd



def Symmetric(k,X,U):	
	hashMap = {}
	ZDD = {}
	def Sym(k,X,U):
		key = tuple([k,tuple(U)])
		if key in hashMap:
			head = hashMap[key]
			return head

		if len(U) == 0 and k ==0:
			val = TrueNode
			head = TrueHash
			hashMap[key] = head
			ZDD[head] = val
			return head

		elif (len(X) == 0 and k > 0) or k < 0:
			val = FalseNode
			head = FalseHash
			hashMap[key] = head
			ZDD[head] = val
			return head

		else:
			v = min(U)
			X0 = [s for s in X if s!=v]
			U0 = [s for s in U if s!=v]
			if v in X:
				head0 = Sym(k,X0,U0)
				head1 = Sym(k-1,X0,U0)
				if head1 == FalseHash:
				 	hashMap[key] = head0
				 	return head0
				else:
					val = tuple([v,head0,head1])
					head = hash2(val)
					hashMap[key] = head
					ZDD[head] = val
					return head
			else:
				head0 = Sym(k,X0,U0)
				if head0 == FalseHash:
					hashMap[key] = head0
					return head0
				else:
					val = tuple([v,head0,head0])
					head = hash2(val)
					hashMap[key] = head
					ZDD[head] = val
					return head

	head = Sym(k,X,U)
	ZDD[0] = head
	return ZDD



def ZDDIntersect(F,G):
	ZDD = {}
	hashMap = {}
	global hashTable
	#hashTable.clear()
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
				head = intersect(fhash,ghash0)
				hashMap[key] = head
				return head


			elif ghash == TrueHash:
				head = intersect(fhash0,ghash)
				hashMap[key] = head
				return head				

			else:
				if v == w:
					head0 = intersect(fhash0,ghash0)
					head1 = intersect(fhash1,ghash1)
					if head1 == FalseHash:
				 		hashMap[key] = head0
				 		return head0

					val = tuple([v,head0,head1])
					head = hash2(val)
					hashMap[key] = head
					ZDD[head] = val
					return head		

				elif v < w:
					head = intersect(fhash0,ghash)
					hashMap[key] = head
					return head		

				else:
					head = intersect(fhash,ghash0)
					hashMap[key] = head
					return head			

	head = intersect(fhash,ghash)
	ZDD[0] = head
	return ZDD

def cycle(ZDD,row):
	if row ==0:
		head = ZDD[0]
		val = ZDD[head]
	else:
		val = ZDD[row]


	if val == TrueNode:
		yield []

	elif val == FalseNode:
		pass

	else:
		v,lo,hi = val
		for x in cycle(ZDD,hi):
			temp = [v]
			temp.extend(x)
			yield temp

		for x in cycle(ZDD,lo):
			temp = [val[0]]
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

def ZDDcontains(ZDD,x):
	y = list(x)
	head = ZDD[ZDD[0]]
	while True:
		if head == FalseNode:
			return False
		elif head == TrueNode and len(y)==0:
			return True
		elif head == TrueNode and len(y) >0:  
			return False

		if head[0] in y:
			y.remove(head[0])
			head = ZDD[head[2]]
		else:
			head = ZDD[head[1]]






			
U = range(729)


ZDD = None
#A = [(1,1,8),(2,3,3),(2,4,6),(3,2,7),(3,5,9),(3,7,2),(4,2,5),(4,6,7),(5,5,4),(5,6,5),(6,4,1),(6,8,3),(7,3,1),(7,8,6),(7,9,8),(8,3,8),(8,4,5),(8,8,1),(9,2,9),(9,7,4)]
#X = [81*(a[0]-1) + 9*(a[1]-1) + a[2]-1 for a in A]
#ZDD = Symmetric(len(X),X,U)
for i in range(81):
	X = range(9*i,9*(i+1))
	A = Symmetric(1,X,U)
	if ZDD == None:
		ZDD = A
	else:
	   ZDD = ZDDIntersect(ZDD,A)

	print i,len(ZDD), ZDDcountSolutions(ZDD)




for r in range(9):
	for q in range(9):
		X = [81*r + 9*c + q for c in range(9)]
		A = Symmetric(1,X,U)
		ZDD = ZDDIntersect(ZDD,A)
		print r,q,len(ZDD), ZDDcountSolutions(ZDD)


for c in range(9):
	for q in range(9):
		X = [81*r + 9*c + q for r in range(9)]
		A = Symmetric(1,X,U)
		ZDD = ZDDIntersect(ZDD,A)
		print c,q,len(ZDD), ZDDcountSolutions(ZDD)


for a in range(3):
	for b in range(3):
		for q in range(9):
			X = []
			for r in range(3*a,3*(a+1)):
				for c in range(3*b,3*(b+1)):
					X.append(81*r + 9*c + q)
			A = Symmetric(1,X,U)
			ZDD = ZDDIntersect(ZDD,A)
			print a,b,len(ZDD), ZDDcountSolutions(ZDD)	









print 5472730538
#A = Symmetric(1,[10*i + q for q in range(10)],U)




