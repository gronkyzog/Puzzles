


for r in range(4,100,4):
	O = (0,0)
	C = (r/4,r/4)
	counter1 = 0
	counter2 = 0
	counter3 = 0
	for x in range(-r,r+1):
		for y in range(-r,r+1):
			if abs(x) + abs(y) <= r and x!=y:
				B = (x,y)
				dot1 = (C[0]*B[0] + C[1]*B[1])
				dot2 = (C[0]-B[0])*(-B[0]) +  (C[1]-B[1])*(-B[1])
				dot3 = (B[0]-C[0])*(-C[0]) +  (B[1]-C[1])*(-C[1])
				if dot1 < 0:
					counter1+=1
				elif dot2 < 0:
					counter2+=1
				elif dot3 < 0:
					counter3+=1

	print '%d,%d,%d,%d,%d' % (r,counter1,counter2,counter3,counter1+counter2+counter3)


