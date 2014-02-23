import itertools
def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def isPerfectSquare(x):
	rx = int(round(x**0.5))
	if (rx**2 - x) ==0:
		return True
	return False

maxsize = 120000

# solve a**2 + b**2 + a*b = c**2  a,b,c integers
# solve x**2 + y**2 + x*y ==1   x,y rational
# (x,y) = (0,-1) is a solution
# y = t*x - 1 # where t is rational slope
# x**2 + (t*x-1)**2 + x*(t*x -1) ==1
# x**2 + t**2*x**2 - 2*t*x + 1 + t*x**2 - x == 1
# x**2(1+t+t**2) - x*2*t ==0
# x =  2*t/(t**2 + t + 1)
# y = (2*t**2 -t**2 - t - 1)/(t**2+t+1)  = (t**2 - t - 1)/(t**2 + t +1)
# let t = m/n

# x = 2*(m/n)/((m/n)**2 + (m/n) + 1)  = 2mn/(m**2 + m*n + n**2)
# y = (m**2 - m*n - n**2)/(m**2 + m*n + n**2)
output = set()
for m in xrange(1,348):
	for n in xrange(1,m):
		if gcd(m,n)!=1:
			continue
		a0 = 2*m*n+ n**2
		b0 = m**2 - n**2
		c0 = m**2 + m*n + n**2
		w =gcd(gcd(a0,b0),c0)
		a0,b0,c0 = a0/w,b0/w,c0/w
		a,b,c = a0,b0,c0
		while a <= 120000 and b <= 120000:
			output.add((a,b))
			output.add((b,a))	
			a,b,c = a+a0,b+b0,c+c0

mapper = {}
for a,b in output:
	if a not in mapper:
		mapper[a] = []
	mapper[a].append(b)


sol = set()
for a,V in mapper.items():
	for b,c in itertools.combinations(V,2):
		if (b,c) in output:
			temp = a+b+c
			if temp <= 120000:
				sol.add(temp)
sol = list(sol)
sol.sort()
for x in sol:
	print x
print sum(sol)



