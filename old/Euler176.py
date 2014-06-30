def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a


def pythagoreantripples(length_max):
 	output = []
 	for m in range(1,length_max):
 		for n in range(1,m):
 			if gcd(m,n)!=1 or (m-n) % 2 ==0:
 				continue

 			ap = 2*m*n
 			bp = m**2 - n**2
 			cp = m**2 + n**2
 			
 			k=1
 			while True:
 				a,b,c = k*ap,k*bp,k*cp
 				if max(a,b) > length_max:
 					break
 				output.append((a,b,c,k,m,n))
 				k+=1
 	return output

def factors(n):
	return [x for x in range(1,n+1) if n % x ==0]






q = 3*5*7
for x in output:
	if x[0]==q or x[1]==q:
		print x