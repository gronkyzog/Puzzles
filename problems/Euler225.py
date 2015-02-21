def f(n,p):
	x,y,z =1,1,1
	for i in xrange(n+1):
		x,y,z = (x+y+z) % p,x,y
		if (x,y,z)==(1,1,1):
			break
		else:
			yield x

def containzero(n,p):
	for s in f(n,p):
		if s ==0:
			return True
	return False

counter = 0
for p in xrange(3,100000,2):
	if  not containzero(10**7,p):
		counter +=1
		print counter,p
		if counter == 124:
			break
