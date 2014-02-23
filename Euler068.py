import itertools
def build_number(x,q=10):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])


Grid = [[0,1,2],
 		[3,2,4],
		[5,4,6],
		[7,6,8],
		[9,8,1]]

A = [0,1,2,3,2,4,5,4,6,7,6,8,9,8,1]

for x in itertools.permutations([1,2,3,4,5,6,7,8,9,10]):
	if x[0] != min([x[0],x[3],x[5],x[7],x[9]]):
		continue
	
	scores = [sum([x[a] for a in G]) for G in Grid]

	min_scores,max_scores = min(scores),max(scores)
	if min_scores==max_scores:
		w = [str(x[a]) for a in A]
		print ''.join(w)


