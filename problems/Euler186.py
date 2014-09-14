

#A = [(100003 - 200003*k + 300007*k**3) % 10**6 for k in range(56)]
#[A.append((A[-24]+A[-55]) % 10**6) for ]

def generator():
	A = []
	for k in range(1,56,2):
		a = (100003 - 200003*k + 300007*k**3) % 10**6
		b = (100003 - 200003*(k+1) + 300007*(k+1)**3) % 10**6
		A.extend([a,b])
		yield [a,b]

	while True:
		a = (A[-24]+A[-55]) % 10**6
		A.append(a)
		b = (A[-24]+A[-55]) % 10**6
		A.append(b)
		A.pop(0)
		A.pop(0)
		yield [a,b]
		

friendMap = set()
for i,(a,b) in enumerate(generator(),start=1):
	friendMap.update([a,b])
	if i%1000==0:
		print i,len(friendMap)
	# try:
	# 	if a==b:
	# 		continue

	# 	newflag = True
	# 	atag = None
	# 	btag = None
	# 	for k,v in friendMap.items():
	# 		if a in v:
	# 			atag = k
	# 			newflag = False
	# 		if b in v:
	# 			btag = k
	# 			newflag = False

	# 	if not newflag:
	# 		if atag is not None and btag is not None:
	# 			if atag < btag:
	# 				friendMap[atag].update(friendMap[btag])
	# 				del friendMap[btag]
	# 			else:
	# 				friendMap[btag].update(friendMap[atag])
	# 				del friendMap[atag]


	# 		elif atag is not None:
	# 			X = friendMap[atag]
	# 			X.add(b)

	# 		elif btag is not None:
	# 			X = friendMap[btag]
	# 			X.add(a)
	# 		else:
	# 			raise Exception('WTF')

	# 	else:
	# 		friendMap[len(friendMap)] = set([a,b])
	# 		print i,len(friendMap),sum([len(v) for v in friendMap.values()])
	# except:
	# 	#print friendMap
	# 	print a,b,atag,btag
	# 	raise 

