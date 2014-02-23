def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


mapper = {}
counter = 0
for m in range(1,2000):
	for n in range(1,m):
		if gcd(m,n)!=1 or (m-n) % 2 ==0:
			continue
		a = m**2 - n**2
		b = 2*m*n
		c = m**2 + n**2
		L = a+b+c
		if L >= 1500000:
			break

		for s in range(L,1500001,L):
			if s not in mapper:
				mapper[s]=1
			else:
				mapper[s] +=1


print len([v for v in mapper.values() if v ==1]) 

