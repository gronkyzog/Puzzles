import csv
import math

def namescore(x):
	return sum([ord(s)-64 for s in x])

csvreader = csv.reader(open('Euler042.txt','rb'),delimiter = ',', quotechar = '\"')

A = []
[A.extend(x) for x in csvreader]

B = [namescore(x)  for x in A]

n = max(B)
imax = int(math.ceil((2.*n)**0.5))
TriNum = set([i*(i+1)/2 for i in range(1,imax+1)])

print  len([b for b in B if b in TriNum])