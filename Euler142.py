def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def isPerfectSquare(n):
	rn = int(round(n**0.5))
	if rn**2 == n:
		return True
	return False


def generate_pythagorean_tripples(cmax):
	output = []
	for m in range(1,cmax):
		for n in range(1,m):
			if gcd(m,n)!=1 or (m-n) % 2 ==0:
				continue
			a = m**2 - n**2
			b = 2*m*n
			c = m**2 + n**2
			for k in range(1,cmax):
				ka,kb,kc = k*a,k*b,k*c
				if kc > cmax:
					break
				temp = [ka,kb,kc]
				temp.sort()
				output.append(temp)
	return output




def run_old(n):
	for a in xrange(1,n):
			print a
			a2 = a**2
			for c in xrange(a%2,a,2):
				if c ==0:
					continue
				c2 = c**2
				for b in xrange(c%2,c,2):
					if b==0:
						continue
					b2 = b**2
					if (a2 + b2)%2 != 0:
						raise
					x = (a2 + b2)/2
					y = (a2 - b2)/2
					z = x-c2
					if isPerfectSquare(a2+b2 - c2):
						if isPerfectSquare(y+z):
							if  isPerfectSquare(y-z):
								print a,b,c,x,y,z
								return x+y+z
# 925,533,117
# a > c > b
def run(cmax):
	P = generate_pythagorean_tripples(cmax)
	trials = []
	for _,b,c in P:
		A = [t for r,s,t in P if r ==c]
		#A.extend([t for r,s,t in P if s ==c])
		for a in A:
			trials.append((a,b,c))


	for b,_,c in P:
		A = [t for r,s,t in P if r ==c]
		A.extend([t for r,s,t in P if s ==c])
		for a in A:	
			trials.append((a,b,c))

	for a,b,c in trials:
		if isPerfectSquare(a**2 + b**2 - c**2):
			x2 = a**2 + b**2
			y2 = a**2 - b**2
			if x2 % 2 ==0 and y2 %2 ==0:
				x,y= x2/2,y2/2
				z = c**2 - x 
				if x>y>z>0:
					print x,y,z,x+y+z


		

		

			





run(1000)


			

