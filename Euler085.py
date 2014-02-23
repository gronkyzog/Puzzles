
def squarecount(m,n):
	return (m+1)*(n+1)*m*n/4

target = 2*10**6
min_error = target
product = 0
for m in range(1,2002):
	a = (m**2 + m)/4.
	b = (m**2 + m)/4.
	c = -target
	n =int(round(-b + (b**2 - 4*a*c)**0.5)/(2*a))
	sc = squarecount(m,n)
	error = abs(target-sc)
	if error < min_error:
		product = m*n
		print product,m,n,error
		min_error = error


print product