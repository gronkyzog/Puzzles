import csv

def namescore(x):
	return sum([ord(s)-64 for s in x])

csvreader = csv.reader(open('Euler022.txt','rb'),delimiter = ',', quotechar = '\"')

A = []
[A.extend(x) for x in csvreader]
A.sort()	
B = [namescore(a) for a in A]
total = sum([(i+1)*b for  i,b in enumerate(B)])
print total
print A[937],namescore(A[937])

