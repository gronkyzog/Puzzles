def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def lcm(a,b):
	k = gcd(a,b)
	return a*b/k


lmax = 1000

counter = 0
for a in range(2,lmax+1):
	for b in range(1,a):
		n,r = divmod(a*b,a+b)
		if r ==0:
			counter +=1
			k = lcm(a,b)
	 		c,d = k/a,k/b
			print counter,a,b,c,d,n





# n = 2*2*3*3*5
# counter = 0
# for a in range(n+1,2*n+1):
# 	b,r  = divmod(n*a,a-n)
# 	if r==0:
# 		counter +=1
# 		k = lcm(a,b)
# 		c,d = k/a,k/b
# 		print counter,a,b,c,d,n
		
# print (5*5*3-1)/2 +1


# # n/a = c/(c+d)
# # n/b = d/(c+d)

# # n/(ac) = n/(ad)

# # ac = ad 


# #1/a + 1/b = 1/n

# # a+b = kab




