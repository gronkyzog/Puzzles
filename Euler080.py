import math

def extract_digits(n,q=10):
	output = []
	r = n
	while r > 0:
		r,s = divmod(r,q)
		output.append(s)
	return output[::-1]

n = 2
rootn = int(n**0.5)

a = 2**(n.bit_length()/2)
b = 1

total = 0
for n in range(1,100):
	rootn = int(n**0.5)
	if rootn**2 == n:
		continue 
	d=1
	a = 2**((n.bit_length())/2)
	b = 1
	counter =0
	while True:
		dold = d
		a,b = a**2 + n*b**2,2*a*b
		d = (a*10**99)/b
		a,b = d,10**99
		counter +=1
		if d == dold:
			break
	sd = sum(extract_digits(d))		
	total += sd
	print n,counter,sd,total

