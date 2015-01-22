
aMap = 'cRdFR'
bMap = 'LFcLd'

def parse(instr):
	direction = 0
	output = []
	for s in instr:
		if s == 'L':
			direction = (direction-1) %4
		elif s == 'R':
			direction = (direction+1) %4
		elif s== 'F':
			output.append(direction)

	return output

def parse2(numarr):
	return (numarr.count(1)-numarr.count(3),numarr.count(0)-numarr.count(2))


D = 'Fa'
for i in range(1,11):
	D = D.replace('a',aMap).replace('b',bMap).replace('c','a').replace('d','b')
	numarr = parse(D)
	print i,parse2(numarr),D
	

print parse2(numarr[:500])