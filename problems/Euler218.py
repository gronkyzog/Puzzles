import eulertools
cmax = 10**16
counter = 0
for i in xrange(1,10**4):
	if i% 100 ==0:
		print i,counter
	for j in range(1,i):
			m  = i**2 - j**2
			n = 2*i*j
			
			a = abs(m**2 - n**2)
			b = 2*m*n
			c = m**2 + n **2
			if c > cmax:
				break
			if eulertools.gcd(a,c)==1 and eulertools.gcd(b,c)==1:
				area = a*b/2
				if area % 6 ==0 and area % 28 ==0:
					pass
				else:
					counter +=1


print counter

# it looks like all are super perfect




# a^2 + b^2  = c^2 + d^2 = L
# (a+c)(a-c) = (d+b)*(d-b) = L-b^2 - d^2





