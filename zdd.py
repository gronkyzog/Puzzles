# (-1,0,0) False
# (-1,1,1) True


#def S(k,U,X):
## to do.
## need to chang the construction of the head
## ZDD[0] points to the head's key. its always an integer. < this ones works better.
## The alternative is that ZDD[0] is the head. when its merged upstream, each of the 2 zeros it needs to be corrected.
import random
import itertools

hashTable = {}
def hash2(x):
	#return hash(x)
	if x in hashTable:
		return hashTable[x]
	else:
		h = len(hashTable)+1
		hashTable[x] = h
		return h

	


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






			


A = [[(5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3), 2], [(3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7), 1], [(5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7), 3], [(9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3), 3], [(4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3), 3], [(3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8), 1], [(4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7), 2], [(7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7), 3], [(8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3), 1], [(2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9), 2], [(8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4), 3], [(6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0), 1], [(6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0), 1], [(6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8), 2], [(2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5), 0], [(2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8), 2], [(5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2), 2], [(1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6), 3], [(4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6), 1], [(3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5), 3], [(1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9), 3], [(2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7), 2]]
#A = [[(7, 0, 7, 9, 4), 0], [(1, 2, 5, 3, 1), 1], [(3, 4, 1, 0, 9), 1], [(9, 0, 3, 4, 2), 2], [(3, 9, 4, 5, 8), 2], [(5, 1, 5, 4, 5), 2]]
A.sort(key=lambda x: x[1])

N = len(A[0][0])
U = range(10*N)



#print ZDDcontains(ZDD,Sol)
ZDD = None

for i in range(N):
	Q = Symmetric(1,[10*i + q for q in range(10)],U)
	if ZDD is None:
		ZDD = Q
	else:
		ZDD = ZDDIntersect(ZDD,Q)
	print i,ZDDcountSolutions(ZDD)



for x,k in A:
	X = [i*10 + q for i,q in enumerate(x)]
	Q = Symmetric(k,X,U)
	if ZDD is None:
		ZDD = Q
	else:
		ZDD = ZDDIntersect(ZDD,Q)
		print x,k,ZDDcountSolutions(ZDD),len(ZDD),len(hashTable)
		








for x in cycle(ZDD,0):
	y = [q-10*i for i,q in enumerate(x)]
	print ''.join([str(q) for q in y])
	break







# # for x,k in A:
# # 	X = [i*10 + q for i,q in enumerate(x)]
# # 	Q = Symmetric(k,X,U)
# # 	ZDD = ZDDIntersect(ZDD,Q)
# # 	print k,x,ZDDcountSolutions(ZDD)




# # print  ZDDcountSolutions(ZDD)



# # for x in cycle(ZDD,0):
# # 	z = tuple([q -10*i for i,q in enumerate(x)])
# # 	print x,z,








	

