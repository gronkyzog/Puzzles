def digitsum(x):
	total = 0
	r = x
	while r > 0:
		r,s = divmod(r,10)
		total  +=s 
	return total 


maxdigits = 20
output = []
for p in range(2,9*maxdigits):
	s = 1
	while  True:
		q = p**s
		if q > 10**(maxdigits-1):
			break
		output.append((q,p,s))
		s +=1

output.sort()
counter = 0
for q,p,s in output:
	if q < 10:
		continue
	if digitsum(q) == p:
		counter +=1
		if counter == 30:
			print counter,q,p,s
			print q
			break