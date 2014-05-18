import itertools 


mapper = {}
for x in itertools.product(range(10),repeat=4):
	sx = sum(x)
	if sx not in mapper:
		mapper[sx] = []
	mapper[sx].append(x)


# for k,v in mapper.items():
# 	print k,len(v)



s = 18
blocks = mapper[s]	

for b0 in blocks:
	b1 = [b for b in blocks if b[0] == b0[0]]
	b2 = [b for b in blocks if b[0] == b0[1]]
	b3 = [b for b in blocks if b[0] == b0[2]]
	b4 = [b for b in blocks if b[0] == b0[3]]
	print b0,len(b1),len(b2),len(b3),len(b4)
