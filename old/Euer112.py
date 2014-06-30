

def ndec(q,k):
	if k ==0:
		return 1

	else:
	  return sum([ndec(s,k-1) for s in range(0,q+1)])

def nasc(q,k):
	if k ==0:
		return 1

	else:
	  return sum([nasc(s,k-1) for s in range(q,10)])



for i in range(10):
	print i,ndec(9,i),nasc(0,i)

# def extract_digits(n,q=10):
# 	output = []
# 	r = n
# 	while r > 0:
# 		r,s = divmod(r,q)
# 		output.append(s)
# 	return output[::-1]




# dec = 0
# asc = 0
# flt = 0
# nmax = 0
# for x in range(0,10**6+1):
# 	dx = extract_digits(x)
# 	n = len(dx)
# 	if n > 1:
# 		dz = [dx[i]-dx[i-1] for i in range(1,n)]
# 	else:
# 		dz = [0]
# 	mindz = min(dz)
# 	maxdx = max(dz)
# 	if (max(dz)==min(dz)==0):
# 		#print 'Flt' ,dx
# 		flt +=1 

# 	if (max(dz) <=0 and min(dz) <=0):
# 		#print 'Dec' ,dx
# 		asc +=1

# 	if (max(dz) >=0 and min(dz) >=0): 
# 		#print 'Asc', dx
# 		dec +=1
# 	if n > nmax:
# 		print n,x,asc,dec,flt,asc+dec-flt
# 		nmax = n

# print  n,x,asc,dec,flt,asc+dec-flt
