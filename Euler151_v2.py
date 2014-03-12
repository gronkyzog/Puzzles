import numpy

def translate(w,i):
	if w[i]>0:
		v = numpy.array(w,dtype=numpy.int32)
		v[i] -=1
		v[i+1:]+=1
		return tuple(v)

def generatestates(x):
	output = set()
	output.add(x)
	n = len(x)
	old = set(output)
	while True:
		new = set()
		for w in old:
			for i in range(n):
				if w[i] > 0:
					new.add(translate(w,i))
		if len(new)==0:
			break
		output.update(new)
		old = set(new)
	return output


def generate_probabilities(w):
	output = {}
	n = len(w)
	total = 1.*sum(w)
	for i in range(n):
		if w[i] > 0:
			tr = translate(w,i)
			if tr not in output:
				output[tr]=0
			output[tr] += w[i]/total

	return output





state = (0,1,0,0,0,0)

A = generatestates(state)
transMap = {a: generate_probabilities(a) for a in A}

stateMap = {k:0 for k in transMap.keys()}
stateMap[state]=1
total =0
for i in range(1,15):
	newMap = {k:0 for k in transMap.keys()}
	for k,v in stateMap.items():
		for s,w in transMap[k].items():
			newMap[s] += v*w
	stateMap = newMap.copy()
	for k,v in stateMap.items():
		if sum(k)==1 and v>0:
			total +=v
			print i,k,v,total

print round(total,6)


