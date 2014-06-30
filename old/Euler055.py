def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


def build_number(x,q=10):
	z = x[::-1]
	return sum([a*q**i for i,a in enumerate(z)])

j=0
for x in range(0,10**4):
	total = x 
	rev = int(str(total)[::-1])
	for i in range(0,51): 
		total += rev 
		rev = int(str(total)[::-1])
		if  total== rev:
			break	
	

	if i >= 50:
		j=j+1
print j
