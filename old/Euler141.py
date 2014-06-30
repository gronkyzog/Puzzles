#n = a**3*b*c**2 + b**2*c
def isPerfectsquare(n):
	rn = int(round(n**0.5))
	if rn**2 == n:
		return True
	return False

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


limit = 10**12
total = 0
for a in xrange(2,10000):
	for b in xrange(1,a):
		if gcd(a,b) > 1:
			continue
		if (a**3*b* + b**2 >= limit):
			break

		for c in xrange(1,10**6):
			n = a**3*b*c**2 + b**2*c
			if n > limit:
				break
			if isPerfectsquare(n):
				total += n
				print total,n,a,b,c