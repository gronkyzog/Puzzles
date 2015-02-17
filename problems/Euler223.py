n = 25*10**6

def generate(a,b,c):
	return [
			(2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a),
			(2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a),
			(2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a)
		   ]


sol = [(1,1,1),(1,2,2)]
new_sol = sol
total = 2
for i in xrange(n):
	temp = []
	for x in new_sol:
		for s in set(generate(*x)):
			if not (s[0]<= s[1]<= s[2]):
				raise 
			if sum(s) <= n:
				temp.append(s)

	if len(temp)==0:
		break
	#sol.extend(temp)
	new_sol = temp
	total = total + len(temp)
	if i% 10000==0:
		print i,len(sol),len(new_sol),total

print total
print 61614848

# import itertools
# import eulertools

# n = 25*10**6
# amax = n/3 +1

# P = eulertools.primesieve(amax)

# A = [0 for a in xrange(amax+1)]
# A[1]=1
# for p in P:
# 	for s in xrange(p,amax+1,p):
# 		if A[s]==0:
# 			A[s]=p


# def prime_factors(A,x):
# 	if x ==0:
# 		return [1]
# 	else:
# 		output = [A[x]]
# 		while x!=A[x]:
# 			x = x/A[x]
# 			output.append(A[x])
# 		return output



# counter = 0
# for a in range(1,amax):
# 	if a% 10000==0:
# 		print a,counter
# 	a2 = a**2 -1
# 	if a2 > 0:
# 		F1 = prime_factors(A,a+1)
# 		F2 = prime_factors(A,a-1)
# 		F = F1+F2

# 		S = list(set(F))
# 		N = [xrange(F.count(s)+1) for s in S]
# 		for E in itertools.product(*N):
# 			f1 = eulertools.product([p**e for p,e in zip(S,E)])
# 			f2 = a2/f1
# 			if (f1+ f2) % 2 ==0 and f1 <= f2:
# 				b,c = (f2-f1)/2,(f1+f2)/2
# 				if a<=b <= c and (a+b+c)<= n:
# 					counter+=1
# 					#print '(%d,%d,%d)' %  (a,b,c)

# print counter + n/2 -1

# counter = 0
# for a in range(1,n+1):
# 	for b in range(a,n+1):
# 		for c in range(b,n+1):
# 			if a+b+c <=n and a**2 + b**2 == c**2 +1:
# 				counter +=1
# 				#print '(%d,%d,%d)' %  (a,b,c)
# print counter








#for i in range(2,1000):
#	print i,eulertools.product(prime_factors(A,i))


# n = 100
# A = [[1] for i in xrange(n+1)]
# for s in xrange(2,n+1):
# 	if s < 100:
# 		print s
# 	for t in xrange(s,n+1,s):
# 		A[t].append(s)


# mapper = {}
# for a in range(1,n-1):
# 	F1 = A[a-1]
# 	F2 = A[a+1]
# 	mapper[a**2-1] = set(x*y for x in F1 for y in F2)



# for k,v in mapper.items():
# 	if k > 0:
# 		print k,max([k % s   for s in v])



#for x,a in enumerate(A):
#	pri
# def nfactors(a):
# 	x == a** 
# 	counter = 0
# 	for s in range(1,x+1):
# 		q,r = divmod(x,s)
# 		if r ==0 and  s < q:
# 			counter +=1

# 	return counter 

# n = 1009
# for a in xrange(n+1):
# 	counter =0
# 	for b in xrange(a,n+1):
# 		for c in xrange(b,n+1):
# 			if a**2 + b**2 == c**2 +1 and (a+b+c)<=n:
# 				#print a,b,c,a+b+c
# 				counter +=1
# 	if counter > 0:
# 		print a,counter,nfactors(a)

# # n = 25*10**6

# A = [[] for n in xrange(n+1)]

# for x in xrange(2,n+1):
# 	for s in xrange(x,n+1,x):
# 		A[s].append(x)


# X = {c**2+1:c for c in xrange(10**6)}

# print 'H'
# for a in range(2,10**2+1):
# 	for b in range(a,10**2+1):
# 		x = a**2 + b**2
# 		if x in X:
# 			c = X[x]
# 			if c >= b:
# 				print '%d,%d,%d' %(a,b,c)


# for p in xrange(1,25*10**6 +1):
# 	for c in xrange(p/3,p/2):
# 		for b in xrange(1,c+1):
# 			a = p - c - b
# 			if a**2 + b**2 - c**2 - 1 ==0:
# 				print p,a,b,c

# # (a+b+c)**2 =  a**2 + b**2 + c**2  + 2*a*b + 2*a+c + 2*b*c 
# # 2*c**2 + 2*a+c + 2*b*c



# for p in range(1,10000,2):
# 	counter =0
# 	for a in range(2,p/3 +1):
# 		for b in range(a,10000):
# 			c = p-a-b
# 			if a<=b<=c:
# 				if a**2 + b**2 == c**2 +1:
# 					#print p,a,b,c
# 					counter +=1

# 			else:
# 				break
# 	if counter > 5:
# 		print p,counter