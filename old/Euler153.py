import datetime

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


n =  10**8
rootn = int(n**0.5)
windowstart = datetime.datetime.now()
print rootn
counter = 0

total = 0
countmap = {}
for x in xrange(1,n+1):
	k = n/x
	total += x*k

windowsend = datetime.datetime.now()
print (windowsend-windowstart).seconds
windowstart = windowsend
for x in xrange(1,rootn+1):
	x2 = x**2
	ymax = int((n - x2)**0.5)
	windowsend = datetime.datetime.now()
	print x,rootn,(windowsend-windowstart).seconds
	windowstart = windowsend
	for y in xrange(1,ymax+1):
		if gcd(x,y)!=1:
			continue
		z = x2+ y**2
		kmax = n/z 
		for k in xrange(1,kmax+1):
			w = k*z
			if w > n:
				break
			counter +=1
			total += 2*k*x*(n/w)	

print 17971254122360635
print total
