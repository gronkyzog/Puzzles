def f(x,p):
	if x ==0:
		return 0
	else:
		total = 0
		while x % p ==0:
			x = x/p
			total +=1
		return total

def run_slow():
	n = 200000

	P2 = [f(i,2) for i in range(n+1)]
	P5 = [f(i,5) for i in range(n+1)]
	F2 = []
	F5 = []
	t2 = 0
	t5 = 0
	for x in range(0,n+1):
		t2 += P2[x]
		t5 += P5[x]
		F2.append(t2)
		F5.append(t5)

	F2 = tuple(F2)
	F5 = tuple(F5)
	threshold = 12
	counter = 0
	for i in xrange(n/3+1):
		T2 = F2[n] - F2[i]
		T5 = F5[n] - F5[i]
		for j in xrange(i,((n-i)/2) +1): 
			k = n-i-j
			if T5 - (F5[j] + F5[k]) >= threshold:
				if T2 - (F2[j] + F2[k]) >= threshold:
					if i==j == k:
						counter +=1
					elif i==j or j==k:
						counter += 3
					else:
						counter +=6
	return counter 
			


print run_slow()