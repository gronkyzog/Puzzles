def primeseive(n):
    # return all primes <= n
    A = [0 for i in range(0,n+1)]
    for i in range(4,n+1,2):
                A[i]=1

    for i in range(3,n+1,2):
        if A[i]==1:
            continue
        else:
            for j in range(2*i,n+1,i): 
                A[j]=1
    return [i for i in range(2,n+1) if A[i]==0]


def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def extended_gcd(a, b):
    x,lastx = 0,1
    y,lasty = 1,0
    while b != 0:
        quotient,_ = divmod(a,b)
        a, b = b, a % b
        (x, lastx) = (lastx - quotient*x, x)
        (y, lasty) = (lasty - quotient*y, y)       
    return (lastx, lasty)

def invmod(a,p):
    x,y = extended_gcd(a,p)
    if  x*a + y*p != 1:
        raise Exception('No inverse: %d mod %d' %(a,p))
    return x

P = [p for p in primeseive(1010000) if p >= 5]
n = len(P)
total = 0
for i in range(1,n):
	p1 = P[i-1]
	p2 = P[i]
	if p1 > 1000000:
		break
	s = len(str(p1))
	k = (invmod(p2,10**s)*p1) % 10**s
	total += k*p2

print total





