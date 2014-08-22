import itertools
import random


#A = [[0, (7, 0, 7, 9, 4)], [1, (1, 2, 5, 3, 1)], [1, (3, 4, 1, 0, 9)], [2, (3, 9, 4, 5, 8)], [2, (5, 1, 5, 4, 5)], [2, (9, 0, 3, 4, 2)]]
A = [[0, (2, 3, 2, 1, 3, 8, 6, 1, 0, 4, 3, 0, 3, 8, 4, 5)], [1, (3, 1, 7, 4, 2, 4, 8, 4, 3, 9, 4, 6, 5, 8, 5, 8)], [1, (3, 8, 4, 7, 4, 3, 9, 6, 4, 7, 2, 9, 3, 0, 4, 7)], [1, (4, 8, 9, 5, 7, 2, 2, 6, 5, 2, 1, 9, 0, 3, 0, 6)], [1, (6, 3, 7, 5, 7, 1, 1, 9, 1, 5, 0, 7, 7, 0, 5, 0)], [1, (6, 9, 1, 3, 8, 5, 9, 1, 7, 3, 1, 2, 1, 3, 6, 0)], [1, (8, 1, 5, 7, 3, 5, 6, 3, 4, 4, 1, 1, 8, 4, 8, 3)], [2, (2, 3, 2, 6, 5, 0, 9, 4, 7, 1, 2, 7, 1, 4, 4, 8)], [2, (2, 6, 1, 5, 2, 5, 0, 7, 4, 4, 3, 8, 6, 8, 9, 9)], [2, (2, 6, 5, 9, 8, 6, 2, 6, 3, 7, 3, 1, 6, 8, 6, 7)], [2, (4, 5, 1, 3, 5, 5, 9, 0, 9, 4, 1, 4, 6, 1, 1, 7)], [2, (5, 2, 5, 1, 5, 8, 3, 3, 7, 9, 6, 4, 4, 3, 2, 2)], [2, (5, 6, 1, 6, 1, 8, 5, 6, 5, 0, 5, 1, 8, 2, 9, 3)], [2, (6, 4, 4, 2, 8, 8, 9, 0, 5, 5, 0, 4, 2, 7, 6, 8)], [3, (1, 7, 4, 8, 2, 7, 0, 4, 7, 6, 7, 5, 8, 2, 7, 6)], [3, (1, 8, 4, 1, 2, 3, 6, 4, 5, 4, 3, 2, 4, 5, 8, 9)], [3, (3, 0, 4, 1, 6, 3, 1, 1, 1, 7, 2, 2, 4, 6, 3, 5)], [3, (4, 2, 9, 6, 8, 4, 9, 6, 4, 3, 6, 0, 7, 5, 4, 3)], [3, (5, 8, 5, 5, 4, 6, 2, 9, 4, 0, 8, 1, 0, 5, 8, 7)], [3, (7, 8, 9, 0, 9, 7, 1, 5, 4, 8, 9, 0, 8, 0, 6, 7)], [3, (8, 6, 9, 0, 0, 9, 5, 8, 5, 1, 5, 2, 6, 2, 5, 4)], [3, (9, 7, 4, 2, 8, 5, 5, 5, 0, 7, 0, 6, 8, 3, 5, 3)]]


def product(A):
	total = 1
	for a in A:
		total *= a

	return total

def generate_points(k,X):
	output = []
	n = len(X)
	Q = 2**10-1
	#Q = set(range(10))
	if k>0:
		for w in itertools.combinations(range(n),k):
			output.append(tuple([2**s  if i in w else Q - 2**s  for i,s in enumerate(X)]))
			#output.append([set([s]) if i in w else Q.difference([s]) for i,s in enumerate(X)])
	else:
		output.append(tuple([Q - 2**s  for s in X]))
		#output.append([Q.difference([s]) for s in X])

	return output


def merge_points(A,B):
	output = []
	for a in A:
		for b in B:
			c =[s&t for s,t in zip(a,b)]
			if 0 not in c:
			#if min([len(s) for s in c])>0:
				output.append(tuple(c))

	return output


def number_possible(A):
	total = 0
	for a in A:
		total += product([bin(s).count('1') for s in a])
	return total


sol = generate_points(*A.pop(0))
print sol
while len(A)>0:
	print '%d,%d' % (len(sol),number_possible(sol))
	temp = generate_points(*A.pop(0))
	sol = merge_points(sol,temp)

print sol

mapper = {2**i:i for i in range(10)}

for x in sol:
	print ''.join([str(mapper[s]) for s in x])
	





