from fractions import Fraction

A = [set([Fraction(60,1)])]
#A = [set([60.])]



for r in range(2,19):
	temp = set()
	n = len(A)
	for i in range(n):
		j = n-i-1
		if i>j:
			break
		for x in A[i]:
			for y in A[j]:
					csum  = x+y
					cprod = x*y
					temp.add(csum) 
					temp.add(cprod/csum)
	print r,len(temp)
	A.append(temp)


print sum([len(a) for a in A])
print len(set.union(*A))


