#x0 = 1.5 = 3/2
# x = 1+1/(1+x)
# a/b = 1+ 1/(1+a/b)
# a/b = 1+ 1/((a+b)/b)
# a/b = 1 + b/(a+b)
# a/b = (a+2b)/(a+b)

def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a





a = 3
b = 2
counter = 0
for i in range(1,1000):
	if len(extract_digits(a)) > len(extract_digits(b)):
		counter +=1
		print counter,i,a,b

	a,b = a+2*b,a+b

