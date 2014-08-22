# (-1,0,0) False
# (-1,1,1) True


#def S(k,U,X):

import itertools


F = [f for f in itertools.combinations(range(10),4)]



def buildZDD(F):
	if len(F)==0:
		val = tuple([-1,0,0])
		head = hash(val)
		return {head:val},head

	elif len(F)==1 and len(F[0])==0:
		val = tuple([-1,1,1])
		head = hash(val)
		return {head:val},head
	else:
		v = min([min(f) for f in [g for g in F if len(g)>0]])
		F0 = [f for f in F if v not in f]
		F1 = [[a for a in f if a!=v] for f in F if v in f]
		Zdd0,head0 = buildZDD(F0)
		Zdd1,head1 = buildZDD(F1)
		
		val = tuple([v,head0,head1])
		head = hash(val)
		Zdd = {head:val}
		Zdd.update(Zdd0)
		Zdd.update(Zdd1)

		


		
		return Zdd,head	

ZDD,head = buildZDD(F)
ZDD[0] = ZDD[head]




def cycle(row):
	node,low,hi = ZDD[row]
	if node ==-1:
		if low==1:
			yield []

	else:
		for x in cycle(low):
			# the current node is not included
			yield x
		for x in cycle(hi):
			# the current node is included
			temp = [node]
			temp.extend(x)
			yield temp




print len(ZDD)
for i,x in enumerate(cycle(0),start=1):
	print i,x



