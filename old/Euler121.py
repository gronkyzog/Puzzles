def f(x,q=2):
	output = []
	r = x
	while r > 0:
		r,q = divmod(r,2)
		output.append(q)

	return output



A = [[1]]
Sol = [None for i in range(201)]
for i in range(11):
	B = []
	for X in A: 
		y = X[-1]
		for x in X:
			temp = list(X)
			last = x+y
			if last > 200:
				continue
			temp.append(last)
			bin = f(last,q=2)
			if len(bin)+sum(bin)-1  < len(temp):
				continue 

			if Sol[last] is None:
				Sol[last] = temp
			

			B.append(temp)
	print i,len(B)
	A = B

Sol[0] = [[0]]
Sol[1] = [[1]]
total = 0
for i,x in enumerate(Sol[1:],start=1):
	if x is not  None:
		total += (len(x)-1)
		print  '%d|%d|%s' %(i,len(x)-1,x)

for i,x in enumerate(Sol[1:],start=1):
	if x is None:
		print i,x

print sum([len(x)-1 for x in Sol if x is not None])
