import math
def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]


total = 0
for i in range(3,9*math.factorial(9)):
	di = extract_digits(i)
	si = sum([math.factorial(s) for s in di])
	if i == si:
		print i,di
		total += i

print total