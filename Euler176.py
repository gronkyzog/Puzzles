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
 			if ap > length_max:
 				break
 			
 			k=1
 			while True:
 				a,b,c = k*ap,k*bp,k*cp
 				if a> length_max or b > length_max:
 					break
 				output.append((a,b,c))
 				k+=1





 	return output


output = pythagoreantripples(100)

for x in output:
	if x[0]==12 or x[1]==12:
		print x