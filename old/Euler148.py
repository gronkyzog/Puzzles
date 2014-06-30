# Use Lucas' Theorem

#nCr(m,n) mod p  =  prod (nCr (m_i,n_i)) mod p
# Where  m_i n_i are the coefficiens of m and  n in base p
# for all 0<=n_i <= m_i   nCr (m_i,n_i) modd p != 0  because m_i, n_i < p and p is prime
# Therefore the number of non zeros mod p for nCm  is the range of  prod (1+m_i),  




def baseQ(n,q):
	output = []
	r = n
	while r > 0:
		r,p = divmod(r,q)
		output.append(p)
	output.reverse()
	return output

def cumsum(a):
	return a*(a+1)/2

def prod(A):
	total = 1
	for a in A:
		total *=(a+1)
	return total


A = baseQ(10**9,7)
print A
total = 0
for i,a in enumerate(A):
	temp= cumsum(a)*(28)**(len(A)-i-1)*prod(A[:i])
	total += temp
	print i,cumsum(a),prod(A[:i]),len(A)-i-1,temp,total
print total

