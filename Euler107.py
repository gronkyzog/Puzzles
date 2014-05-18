import csv
import numpy



def getnewavailable(A,nodes):
	output = []
	for a in nodes:
		for i,x in enumerate(A[a]):
			if x > 0 and i not in nodes:
				output.append((A[a,i],a,i))

	output.sort()
	return output


csvreader = csv.reader(open('Euler107.txt','rb'),delimiter = ',')
network =[]
for X in csvreader:
	network.append([int(a) if a.isdigit() else 0 for a in X])

A = numpy.array(network)


nodes = [0]
connections = []
newnodes = getnewavailable(A,nodes)
while len(newnodes) > 0:
	nodes.append(newnodes[0][2])
	connections.append(newnodes[0])
	print nodes,sum([x[0] for x in connections])
	newnodes = getnewavailable(A,nodes)

print numpy.sum(A)/2 - sum([x[0] for x in connections])