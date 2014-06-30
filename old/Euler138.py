def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


mapper = {}
counter = 0

x,y = 2,1

total = 0
for i in range(0,12):
	m,n = x + 2*y,y
	h = m**2 - n**2
	b = 2*m*n
	L = m**2 + n**2
	total += L
	print i,h,b,L,total
	x,y = 2*x + 5*y,2*y + x

print total