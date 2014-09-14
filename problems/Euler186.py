def generator():
	A = []
	for k in range(1,56):
		a = (100003 - 200003*(k) + 300007*(k)**3) % 10**6
		A.append(a)
		yield a

	while True:
		a = (A[-24]+A[-55]) % 10**6
		A.append(a)
		A.pop(0)
		yield a
		


A = {524287:0}
B = {0:set([524287])}

nmax = max(A.values())
gen = generator()
i=0
while True:
	a = next(gen)
	b = next(gen)
	if a==b:
		continue
	i+=1
	# print i,a,b
	# if i>20:
	# 	break
	if a == b:
		continue
	if a not in A and b not in A:
		nmax +=1
		n = nmax
		a_id = n
		b_id = n

		A[a] = n
		A[b] = n
		B[n] = set([a,b])

	elif a in A and b in A:
		a_id = A[a]
		b_id = A[b]
		if a_id < b_id:
			for s in B[b_id]:
				A[s] = a_id
			B[a_id].update(B[b_id])
			del B[b_id]

		elif a_id > b_id:
			for s in B[a_id]:
				A[s] = b_id
			B[b_id].update(B[a_id])
			del B[a_id]
		else:
			continue
	
	elif a in A:
		a_id = A[a]
		A[b] = a_id
		B[a_id].add(b)


	elif b in A:
		b_id = A[b]
		A[a] = b_id
		B[b_id].add(a)

	if a_id == 0 or b_id ==0:
		length = len(B[0])
		if length >= 990000:
			print i,length
			break

print 2325629