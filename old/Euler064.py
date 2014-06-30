def cont_frac_root(n):
	m = int(n**0.5)
	if m*m == n:
		return m,[]
	output = m
	digits = []
	x=1
	y = m
	while True:
		x = (n-y*y)/x
		digits.append((m+y)/x)
		y = m - ((m+y)%x)

		if x <=1:
			return output,digits

counter = 0
for i in range(2,10001):
	a,d = cont_frac_root(i)	
	ld = len(d)
	print i,a,d
	if ld % 2 == 1:
		counter +=1

print counter





	




