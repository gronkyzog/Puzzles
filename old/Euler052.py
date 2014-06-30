import numpy

def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]

def digit_frequency(x):
	dx = extract_digits(x)
	return tuple([dx.count(i) for i in range(0,10)])



for x in range(10**5,10**6):
	x2 = 2*x
	fx = digit_frequency(x)
	fx2 = digit_frequency(2*x)
	if fx == fx2:
		A = set([digit_frequency(i*x) for i in range(1,7)])
		if len(A) == 1:
			print [i*x for i in range(1,7)]
			break
	



		
	






