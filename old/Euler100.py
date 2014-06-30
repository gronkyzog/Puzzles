
def int_root(n):
	a = 2**(n.bit_length()/2)
	b = 1
	while True:
		ea,eb =a**2 - n*b**2,2*a*b
		a,b = 2*a**2 -ea,eb
		if abs(ea) < abs(eb):
			x = a/b
			return x,x**2==n


def pell(n):
	# solves x^2 - ny^2 = 1
	# x,y are integers
	m,perfect = int_root(n)
	if perfect:
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
		
		if z ==1:
			return h,k

		y = m - ((m+y)%x)
		hp,hpp = h,hp
		kp,kpp = k,kp


#2*(2*x -1)**2  -1 = c**2


n = 2
x,y = pell(n)

x1,y1 = x,y
output = [(x1,y1)]
for i in range(0,3):
	x,y = x1*x + n*y1*y,x1*y + y1*x
	output.append((x,y))


for x,y in output:
	print x,y,x**2 - n*y**2
print '---------------'






# 2a(a-1) = n(n-1)
# n^2 - n -2*a^2 + 2*a = 0
#(+1 + sqrt(1 + 8*(a^2 - a)))/2

# +1 +/- sqrt(4 + 8(a^2 -a))/2



for a in range(0,100):
	f = 8*a**2 - 8*a + 1
	rootf,perfect = int_root(f)
	if perfect:
		print a,rootf







