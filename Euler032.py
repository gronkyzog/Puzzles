def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]


total = set()
for i in range(1,100):
	di = extract_digits(i)
	a = len(di)
	for j in range(i,10000):
		k = i*j
		
		dj = extract_digits(j)
		dk = extract_digits(k)
		dall = set(di).union(dj).union(dk)
		if len(dall) ==9 and len(di)+len(dj)+len(dk)==9 and 0 not in dall:
			print '%dx%d=%d' %(i,j,k)
			total.add(k)

print sum(total)

