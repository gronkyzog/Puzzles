import csv
import math
import itertools

def extract_digits(n,q=10):
	output = []
	r = n
	while r > 0:
		r,s = divmod(r,q)
		output.append(s)
	return output[::-1]

def index_all(A,x):
	# returns all locations of x in A:
	n = A.count(x)
	output = []
	s = -1
	for i in range(n):
		s= A.index(x,s+1)
		output.append(s)

	return tuple(output)



def build_permutation(x,y):
	# build the coordinate permutation if x -> y
	# returns null if x and y are not permutations
	# repeats  get grouped [2,(1,4),3]  states that 1 and 4 are the same symbol
	sx = set(x)
	sy = set(y)

	if sx != sy:
		return None

	fx = tuple([x.count(s) for s in sx])
	fy = tuple([y.count(s) for s in sy])
	if fx != fy:
		return None
	
	chars = []
	for s in x:
		if s not in chars:
			chars.append(s)
	
	output = [(index_all(x,s),index_all(y,s)) for s in chars]
	return tuple(output)




def solve():
	csvreader = csv.reader(open('Euler098.txt','rb'),delimiter = ',',quotechar = '"')

	data = []
	for x in csvreader:
		data.extend(x)


	freq_map = {}
	characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for x in data:
		key = tuple([x.count(s) for s in characters])
		if key not in freq_map:
			freq_map[key] = []
		freq_map[key].append(x)


	A = [x**2 for x in range(1,10**4)]
	digit_map = {}
	for a in A:
		da = extract_digits(a)
		key = tuple([da.count(s) for s in range(10)])
		if key not in digit_map:
			digit_map[key] = []
		digit_map[key].append(a)


	digit_permutationmap = {}
	for k,v in digit_map.items():
		if len(v) >=2:
			for x,y in itertools.combinations(v,2):
				perm = build_permutation(extract_digits(x),extract_digits(y)) 
				if perm is None:
					continue

				if perm not in digit_permutationmap:
					digit_permutationmap[perm] = []
				digit_permutationmap[perm].append((x,y))

	freq_permutationmap = {}
	for k,v in freq_map.items():
		if len(v) >=2:
			for x,y in itertools.combinations(v,2):
				perm = build_permutation(x,y) 
				if perm is None:
					continue
				if perm not in freq_permutationmap:
					freq_permutationmap[perm] = []
				freq_permutationmap[perm].append((x,y))


	max_square = 0
	for k,v in freq_permutationmap.items():
		if k in digit_permutationmap:
			numbers = digit_permutationmap[k]
			max_num = max([max(s) for s in numbers])
			if max_num > max_square:
				print k,v,numbers,max_num
				max_square = max_num
				
	print max_square

solve()


