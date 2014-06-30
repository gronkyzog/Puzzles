
def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]


def build_number(x,q=10):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])

def isPandigital(x):
	dx = extract_digits(x)
	sx = set(dx)
	if len(sx)==9 and len(dx)==9 and 0 not in sx:
		return True
	else:
		return False

maxoutput = 0
for i in range(1,100000):
	output = ''
	for j in range(1,10):
		output += str(i*j)
		if  isPandigital(int(output)):
			if int(output) > maxoutput:
				maxoutput = int(output)
			print i,j,output
		elif len(output) >9:
			break
print maxoutput
		
	
