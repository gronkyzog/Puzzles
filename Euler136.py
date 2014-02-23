#n = x1*x2
# b**2 - (a+b)**2 - (2*a*b)**2 = n
# b**2 - a**2 - 2*a*b - b**2 - 4*a**2 - 4*a*b - b**2 = n
# -b**2 -5*a**2 -6*a*b = n
# 5*a**2 + 6*a*b + b**2 + n =0
# a = (-6*b +/- sqrt(36*b**2 - 20*(b**2 + n))/10
# a = (-6*b +/- sqrt(16*b**2 - 20*n))/10

#the inners of sqrt must be a  must be a perfect square
# 16*b**2 - 20*n = c**2
# a = (-6*b +/- c)/10
# 10*a = -6b +c 

# c = 10*a + 6*b

# 20*n = 16*b**2 - c**2
# 20*n = (4*b +c)*(4*b-c)

# 20*n = (4*b+ 10*a + 6*b)*(4*b -10*a - 6*b)
# 20*n = (10*b + 10*a)*(-2*b - 10*a)
# 20*n = -20*(b + a)*(b + 5*a)
# n = -(b+a)*(b+5*a)
# n = (b+a)*(-b - 5*a)

def Factors(n):
	passcount = 0
	failcount = 0
	output = [0 for s in range(n+1)]
	for p in range(1,n+1):
		for s in range(p,n+1,p):
			sp = s/p
			x1 = p
			x2 = sp
			if (x1+x2) % 4 ==0 and 3*x1 - x2 > 0:
				output[s]  +=1
				passcount +=1
			else:
				failcount +=1

	return output

def Factors2(n):
	output = [0 for s in range(n+1)]
	for x1 in range(1,n+1):
		e = x1 % 4
		e = 4-e
		for x2 in range(e,min(3*x1,n/x1+1),4):
			s = x1*x2
			output[s] +=1
	return output




B = Factors2(50*10**6)
print len([b for b in B if b==1])

