from fractions import Fraction


def solutions(target,A):
	print target,len(A)
	if sum(A) > target and A[-1] < target:
		output = []
		for i,a in enumerate(A):
			if a < target:
				sol = solutions(target-a,A[(i+1):])
				[s.append(a) for s in sol]
				output.extend(sol)
			if a==target:
				output.append([a])

		return output

	else:
		return []




n = 30
target = Fraction(1,2)
A = [Fraction(1,s**2) for s in range(1,n+1)]

sol = solutions(target,A)

print sol