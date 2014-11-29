import math

def int_root(n):
	# find the biggest x such that x**2 < n
	x = int(n**0.5)
	x2 = x**2
	if x2==n:
		return x-1
	elif x2 < n:
		while x2 <n:
			x+=1
			x2 = x**2
		return x-1

	else:
		while x2 >n:
			x-=1
			x2 = x**2
		return x	



def gauss_circle(r2):
	# find all points inside (not on) a boundard of radius r, specified as r2= r**2
	r = int_root(r2)
	total = 1+4*r
	for i in range(1,r+1):
		if i% 1000000==0:
			print i
		total += 4*int_root((r2-i*i))
	
	return total

def f(r):
	return 3*r**2/2 -r/4 +1+ gauss_circle(r**2/32)


print f(10**9)


#Generate all points and test for negative products
# for r in xrange(8,1000,8):
# 	O = (0,0)
# 	C = (r/4,r/4)
# 	counter1 = 0
# 	counter2 = 0
# 	counter3 = 0
# 	for x in range(-r,r+1):
# 		for y in range(-r,r+1):
# 			if abs(x) + abs(y) <= r and x!=y:
# 				B = (x,y)
# 				dot1 = (C[0]*B[0] + C[1]*B[1])
# 				dot2 = (C[0]-B[0])*(-B[0]) +  (C[1]-B[1])*(-B[1])
# 				dot3 = (B[0]-C[0])*(-C[0]) +  (B[1]-C[1])*(-C[1])
# 				if dot1 < 0:
# 					counter1+=1
# 					#print '%d,%d' % (x,y)
# 				elif dot2 < 0:
# 					counter2+=1
# 					#print '%d,%d' % (x,y)
# 				elif dot3 < 0:
# 					counter3+=1
# 					#print '%d,%d' % (x,y)
# 	print '%d,%d,%d' %(r,counter1+counter2+counter3,f(r))

