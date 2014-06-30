
def extract_digits(x,q):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


def build_number(x,q):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])

total = 0
for i in range(0,10**6):
	d2 = extract_digits(i,2)
	d10 = extract_digits(i,10)
	if d2 == d2[::-1] and d10 == d10[::-1]:
		print i,d2,d10
		total += i
print total