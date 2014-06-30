
mapper ={}
for x in range(1,10):
	key = tuple ([1 if s==x else 0 for s in range(10)])
	mapper[key]=1


print '%d,%d,%d' % (1,len(mapper),sum(mapper.values()))

for r in range(2,19):
	temp = {}
	for k,v in mapper.items():
		for x in range(10):
			key = tuple([k[s]+1 if s==x else k[s] for s in range(10)]) 
			if max(key) <= 3:
				if key not in temp:
					temp[key]=0
				temp[key] += v
	mapper = temp
	print '%d,%d,%d' %(r,len(mapper),sum(mapper.values()))


print sum(mapper.values())
