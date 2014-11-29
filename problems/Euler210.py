# import math
def gauss_circle(r):
	total = 1+4*int(r)
	r2 = r**2
	for i in xrange(1,int(r)):
		total += 4*int((r2-i**2)**0.5)

	return total



# def f(r):
# 	return (3*r**2)/2 - (r/4) + 1 +  gauss_circle((2**0.5*r)/8)


# #Generate all points and test for negative products
# for r in range(8,1000,8):
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

# 	print r,counter1+counter2+counter3,f(r)


print gauss_circle(100**0.5)



# r = 10**9
# old_tot=0
# printflag = False
# counter = 0
# for i in xrange(10**8,r+1):
# 	tot = (r**2)/(4*i+1)  - (r**2)/(4*i+3)
# 	if tot == old_tot:
# 		counter +=1
# 		printflag = True
# 	else:
# 		if printflag:
# 			print i,tot,counter
# 		counter=0
# 		printflag = False

# 	old_tot = tot

