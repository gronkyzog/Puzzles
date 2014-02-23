def isprime(n):
    # return all primes <= n
    A = [1 for i in range(0,n+1)]
    A[0]=0
    A[1]=0
    for i in range(4,n+1,2):
                A[i]=0

    for i in range(3,n+1,2):
        if A[i]==0:
            continue
        else:
            for j in range(2*i,n+1,i): 
                A[j]=0
    return A



def tile(r,a):
	if r == 0:
		return 1
	else:
		radius = 3*r*r - 3*r + 2
		return radius + (a % (6*r))


def neighbours(r,a):
	if r ==0:
		return [2,3,4,5,6,7]
	else:
		s,k = divmod(a,r)

		if k==0:
			return [tile(r+1,a+s-1),tile(r+1,a+s),tile(r+1,a+s+1),tile(r,a-1),tile(r,a+1),tile(r-1,a-s)]
		else:
			return [tile(r+1,a+s),tile(r+1,a+s+1),tile(r,a-1),tile(r,a+1),tile(r-1,a-s),tile(r-1,a-s-1)]


#print tile(2,8)
#print neighbours(2,8)

P = isprime(1000000)
print P[:10]
counter = 1
for r in range(1,100000):
	for a in [0,6*r-1]:
		x = tile(r,a)
		B = neighbours(r,a)
		diff = [abs(b-x) for b in B]
		primes = sum([P[b] for b in diff])
		if primes ==3:
			counter +=1
			print x,counter,primes,r,a
			if a !=0 and 6*r-1 != a:
				raise Exception('WTF')
		if counter == 2000:
			break
	if counter == 2000:
		break

