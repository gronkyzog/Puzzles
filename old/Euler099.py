import csv
import math
import numpy
csvreader = csv.reader(open('Euler099.txt','rb'),delimiter = ',')

pairs = []
for i,row in enumerate(csvreader):
	pairs.append((int(row[0]),int(row[1])))

logs = []
for x in pairs:
	logs.append(math.log(x[0])*x[1])

I = numpy.argsort(logs)

I = I[::-1]
print I[0]+1,pairs[I[0]],logs[I[0]]
print I[1]+1,pairs[I[1]],logs[I[1]]
		

