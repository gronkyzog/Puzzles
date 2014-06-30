from fractions import Fraction
import itertools

def powerset(iterable):
   s = list(iterable)
   return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1,len(s)+1))


n = 45


P = [3,5,7,11,13,17,19,23,29,31,37,39,41,43,47,49,53,59,61,67,71,73,79]
P.reverse()


excluded = set()
A = [i for i in range(2,n+1)]
for p in P:
	B = [Fraction(1,a**2) for a in A if a%p ==0]
	B = [b for b in B if b not in excluded]
	output  = set()
	for i,x in enumerate(powerset(B)):
		y = sum(x)
		if y.denominator % p != 0: 
			output.update(x)
	
	excluded.update(set(B).difference(output))				
	print p,len(B),len(excluded)

C = [i for i in range(1,n+1) if Fraction(1,i**2) not in excluded]
print len(C),C
# def solutions(target,A):
# 	print target,len(A )
# 	if sum(A) > target and A[-1] < target:
# 		output = []
# 		for i,a in enumerate(A):
# 			if a < target:
# 				sol = solutions(target-a,A[(i+1):])
# 				[s.append(a) for s in sol]
# 				output.extend(sol)
# 			if a==target:
# 				output.append([a])

# 		return output

# 	else:
# 		return []




# n = 30
# target = Fraction(1,2)
# A = [Fraction(1,s**2) for s in range(1,n+1)]

# sol = solutions(target,A)

# print sol