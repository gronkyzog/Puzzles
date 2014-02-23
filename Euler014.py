
maxLen = 0
for i in range(2,1000000):
	counter = 1
	z=i
	while z!= 1:
		if z%2 ==0:
			z = z/2
		else:
			z = 3*z + 1
		counter +=1
	if counter > maxLen:
		maxLen = counter 
		print i,maxLen
	