counter = 0
output = set()
n = 100000
for p in range(1,n):
	if p% 1000==0:
		sx = min(len(output),150000)
		print p,sx,len(output),sorted(list(output))[sx-1]
	for q in range(p+1,2*p+1):
		r,s = divmod(1+p*q,q-p)
		if s ==0:
			A = p*q*r
			output.add(A)

print len(output)
print sorted(list(output))[150000-1]
#print 196565502887779200





# import eulertools

# n = 1000000
# R = [r**2 + 1 for r in range(n+1)]
# P = eulertools.primesieve(n)
# R = [[1] for r in range(n+1)]
# for p in P:
# 	soln = eulertools.modsqrt_prime(-1,p)
# 	for s in soln:
# 		for k in xrange(s,n+1,p):
# 			r2 = k**2 +1
# 			R[k].append(p)
# 			R[k].append(r2/p)
# 			R[k].append(-p)
# 			R[k].append(-r2/p)


# output = set()
# for r,X in enumerate(R):
# 	r2 = r**2 +1
# 	for x in X:
# 		p = x+r
# 		if r2%x !=0:
# 			raise
# 		q = (r2/x) + r
# 		A = abs(r*p*q)
# 		if p*q - p*r - q*r != 1:
# 			raise
# 		output.add(A)

# print sorted(list(output))[150000]
# print 1884161251122450		
