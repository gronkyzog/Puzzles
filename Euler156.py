#import itertools

def split(x,q):
	output = []
	z = x
	while z>0:
		z,r = divmod(z,q)
		output.append(r)
	return output


def score(n,s):
	#s=1
	X = split(n,10)
	total = 0
	if n ==0:
		return 0
	z = n+1
	for i,x in enumerate(X):
		loops = (z/10**(i+1))*10**i
		residual = max(min(10**i,(z % 10**(i+1))-s*10**i),0)
		total += loops + residual
	return total


def scan(lb,ub,s,k=0):
	output = []
	if ub-lb <2:
		for x in range(lb,ub+1):
			if score(x,s)==x:
				output.append(x)
		return output


	mp = (lb+ub)/2

	slb = score(lb,s)
	sub = score(ub,s)
	smp = score(mp,s)

	if (slb <= lb  <= smp) or (mp >= slb >= lb):
		output.extend(scan(lb,mp,s,k+1))
	
	if (smp <= mp  <= sub) or (ub >= smp >= mp):
		output.extend(scan(mp,ub,s,k+1))
	

	return output

total = 0
for s in range(1,10):
	print s
	temp = sum(set(scan(0,10**30,s)))
	total += temp

print total




# for i in range(10**6):
# 	s = score(i,1)
# 	if i==s:
# 		print i