import itertools 
import csv


def test_set(A):
	n = len(A)
	pos_map = {}
	for i in range(1,n+1):
		pos_map[i]= {}
		for x in itertools.combinations(A,i):
			sx = sum(x)
			if sx in pos_map[i]:
				return False
			else:
				pos_map[i][sx] = x
	
	for i in range(1,n):
		if max(pos_map[i].keys()) >= min(pos_map[i+1].keys()):
			return False

	return True




#print test_set([81, 88, 75, 42, 87, 84, 86, 65])
#print test_set([157, 150, 164, 119, 79, 159, 161, 139, 158])


csvreader = csv.reader(open('Euler105.txt','rb'),delimiter = ',')


total = 0
for x in csvreader:
	A = [int(s) for s in x]
	if test_set(A):
		total += sum(A)

print total
