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

 			for k in range(1,length_max):
	 			a = k*2*m*n
	 			b = k*m**2 - n**2
	 			c = k*m**2 + n**2
	 			output.append((a,b,c)) 



 	return output


print pythagoreantripples(10)