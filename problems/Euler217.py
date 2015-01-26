import eulertools 
def S(n):
	return n*(n+1)/2
def build_head(length):
	head = {(q,q):(q,1) for q in range(0,10)}
	for k in range(1,length):
		temp = {}
		for (h,ds),v in head.items():
			sx,nx = v[0],v[1]
			for q in range(10):
				key = tuple([h,ds+q])
				if key not in temp:
					temp[key] = (0,0)
				sy,ny = temp[key]
				temp[key]= (sy+sx*10 +nx*q,ny+nx)
		head = temp
	return head



def build_tail(length):
	tail = {(q,q):(q,1) for q in range(1,10)}
	for k in range(1,length):
		temp = {}
		for (h,ds),v in tail.items():
			sx,nx = v[0],v[1]
			for q in range(10):
				key = tuple([q,ds+q])
				if key not in temp:
					temp[key] = (0,0)
				sy,ny = temp[key]
				temp[key]= (sy+sx*10 +nx*q,ny+nx)
		tail = temp
	return tail



def build_balanced(length):
	n = length/2 + length%2
	A = build_head(n)
	B = build_tail(n)
	if length % 2 == 1:
		total = 0
		keys = set(A.keys()).intersection(B.keys())
		for k in keys:
			sa,na = A[k]
			sb,nb = B[k]
			#print '%d,%d,%d' %(k[0],k[1],sa*nb + sb*na*10**(n-1) - k[0]*10**(n-1)*na*nb)
			total += sa*nb + sb*na*10**(n-1) - k[0]*10**(n-1)*na*nb
		return total
	else:
		Anew = {}
		Bnew = {}
		for (_,k),(sx,nx) in A.items():
			if k not in Anew:
				Anew[k] = (0,0)
			sy,ny = Anew[k]
			Anew[k] = (sx+sy,nx+ny)

		for (_,k),(sx,nx) in B.items():
			if k not in Bnew:
				Bnew[k] = (0,0)
			sy,ny = Bnew[k]
			Bnew[k] = (sx+sy,nx+ny)

		keys = set(Anew.keys()).intersection(Bnew.keys())
		total = 0
		for k in keys:
			sa,na = Anew[k]
			sb,nb = Bnew[k]
			#print k,sa,na,sb,nb,sa*nb + sb*na*10**n
			total += sa*nb + sb*na*10**n 
		return total

total = 0
for i in range(1,48):
	total += build_balanced(i)
	print i,total % (3**15)

total = total % (3**15)
print total