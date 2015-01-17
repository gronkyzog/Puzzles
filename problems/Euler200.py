import eulertools

def prime_proof(x):
	sx = str(x)
	n = len(sx)
	for i in range(n):
		if i==0:
			Q = (1,2,3,4,5,6,7,8,9)
		else:
			Q = (0,1,2,3,4,5,6,7,8,9)

		for q in Q:
			sy = list(sx)
			sy[i] = str(q)
			y = int(''.join(sy))
			if eulertools.is_prime(y):
				return False
	return True

P = eulertools.primesieve(10**6)



output = []
qMax = 10**12
for p1 in P:
	for p2 in P:
		if p1!=p2:
			q = (p1**2)*(p2**3)
			if q > qMax:
				break

			output.append((q,p1,p2))

output.sort()

print len(output)
output = [s for s in output if '200' in str(s[0])]
print len(output)
output = [s for s in output if prime_proof(s[0])]
print len(output)
for i,x in enumerate(output,start=1):
	print i,x