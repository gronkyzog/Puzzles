def pell_bf(n):
	for y in xrange(1,10**7):
		x = int((1+n*y*y)**0.5)
		e = x**2 - n*y**2
		if e==1:
			return (x,y)

def pell(n):
	m = int(n**0.5)
	if m*m == n:
		return None,None
	output = m
	x=1
	y = m
	hp,hpp = m,1
	kp,kpp = 1,0
	while True:
		x = (n-y*y)/x
		a = ((m+y)/x)
		h,k = a*hp + hpp,a*kp + kpp
		z = h**2 - n*k**2
		#print x,y,a,h,k,z
		
		if z ==1:
			return h,k

		y = m - ((m+y)%x)
		hp,hpp = h,hp
		kp,kpp = k,kp

		#if x <=1:
		#	return None,None


max_x = 0
max_i = 0
for i in range(2,1001):
	if int(i**0.5)**2 == i:
		continue
	x,y = pell(i)
	if x > max_x:
		print i,x,y
		max_x = x



