def build_number(x,q=10):
	A = x[::-1]
	return sum([a*q**i for i,a in enumerate(A)])


def product(A):
	total = 1
	for a in A:
		total *=a
	return total

def cycle(A,k):
	if k==1:
		for a in A:
			yield [a]
	else:
		for a in A:
			B = [b for b in A if b!=a]
			for x in cycle(B,k-1):
				output = [a]
				output.extend(x)
				yield output

def cycleRestricted(A,F,k):
	if len(F)==1:
		#print A,F
		for x in cycle(A,k):
			if build_number(x) % F[0] ==0:
				yield x
	else:
		for a in A:
			B = [b for b in A if b!=a]
			for x in  cycleRestricted(B,F[1:],k-1):
				if (100*a + 10*x[0] + x[1]) % F[0] ==0:
					output = [a]
					output.extend(x)
					yield output				


A = [0,1,2,3,4,5,6,7,8,9]
F = [1,2,3,5,7,11,13,17]


total = 0
print '----------------------------'
for x in cycleRestricted(A,F,10):
	total +=  build_number(x)
	print x,total

	
