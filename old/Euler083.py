# finds the least cost path from  a set of known start to known finish

import csv
import numpy

csvreader =csv.reader(open('Euler083.txt'),delimiter = ',')

cost = []
for row in csvreader:
	int_row = [int(x) for x in row]
	cost.append(int_row)

cost = numpy.array(cost,dtype = numpy.int32)

m,n = cost.shape
total = numpy.zeros([m,n],dtype = numpy.int32)

startpoints = set([(0,0)])
endpoints  = set([(79,79)])


mesh = [(-1,0),(1,0),(0,-1),(0,1)]

#mesh = [(-1,0),(0,-1)]

# Starting with some path that may or may not be valid be valid
for s in startpoints:
	total[s] = cost[s]
for i in range(1,m):
	total[i,0] = total[i-1,0] + cost[i,0]
for i in range(0,m):
	for j in range(1,n):
		total[i,j] = total[i,j-1] + cost[i,j]

counter = 0
print 'Initial Solution:%d' % min([total[x,y] for x,y in endpoints])
while True:
	changeFlag = False
	for i in range(0,m):
		for j in range(0,n):
			if (i,j) in startpoints:
				continue
			else:
				adj_mesh = [(i+x,j+y) for x,y in mesh if i+x >=0 and i+x < m and j+y >=0 and j+y < n]
				trial = min([total[x,y] for x,y in adj_mesh]) + cost[i,j]
				if trial != total[i,j]:
					changeFlag = True
					total[i,j] = trial
	if changeFlag == False:
		# no changes where made, stop the program
		break
	counter +=1
	print counter,min([total[x,y] for x,y in endpoints])


