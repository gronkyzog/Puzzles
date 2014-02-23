import itertools 


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)+1))


n = 12


A = [i for i in range(n)]

B = [x for x in powerset(A)]

#C = [z for z in itertools.combinations(B,2) if len(z[0]) == len(z[1]) and len(set(z[0]).intersection(z[1]))==0]
#C = [z for z in itertools.combinations(B,2) if len(z[0]) == len(z[1])]
C = []
for k in range(1,n):
	print k
	B = [x for x in itertools.combinations(A,k)]
	C.extend([z for z in itertools.combinations(B,2) if  len(set(z[0]).intersection(z[1]))==0])




print len(C) 




print len(C)
counter = 0
for x,y in C:
	for r,s in zip(x,y):
		if r > s:
			#print x,y,r,s
			counter +=1
			break
print counter