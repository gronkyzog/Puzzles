import array
def cycle(x):
	z = x
	counter = 0
	while z> 1:
		if z%2 ==0:
			z = z/2
		else:
			z = 3*z + 1
		counter +=1
	return counter		

def test():
	n = 10**6
	A = [0 for i in xrange(n)]
	for x in range(2,n):
		if A[x]!= 0:
			continue
		z = x
		seq = [z]
		while True:
			z = z/2 if z % 2==0 else 3*z +1
			if z<n:
				if A[z]!=0 or z==1:
					for i,s in enumerate(seq):
						if s < n:
							A[s] = i+ A[z]+1
					break

			seq.insert(0,z)

	B = sorted((v, i) for (i, v) in enumerate(A))
	return B[-1][1]

if __name__ == '__main__':
    print test()