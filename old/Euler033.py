import numpy
def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]

def build_number(x):
	A = x[::-1]
	return sum([a*10**i for i,a in enumerate(A)])

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


def cancel_digits(a,b):
	da = extract_digits(a)
	db = extract_digits(b)
	for i in range(1,10):
		while da.count(i) > 0 and db.count(i) > 0:
			da.remove(i)
			db.remove(i) 

	return build_number(da),build_number(db)

pi = 1
pj = 1
for i in range(10,99):
	for j in range(i+1,99):
		xi,xj = cancel_digits(i,j)
		if i*xj == xi*j and i != xi and xi != 0:
			pi *= i
			pj *= j
			print i,j,xi,xj

g = gcd(pi,pj)
print pi,pj,pi/g,pj/g