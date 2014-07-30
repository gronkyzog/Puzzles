import eulertools




p = 23

for x in range(1,p-1):
	for k in range(1,p):
		if pow(x,k+1,p)==x:
			print x,k
			break




