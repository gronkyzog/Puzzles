def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


print max([sum(extract_digits(a**b)) for a in range(0,100) for b in range(0,100)])