def is_perfect_square(x):
	y = int(x**0.5)
	return  y**2 == x


def get_triangles(s):
	#solves for k2mn =  and k(m**2 - n**2)
	output = []
	for i in range(1,2*s +1):
		if is_perfect_square(s**2 + i**2):
			for j in range(1,s):
				if j <= s and  i-j <= s and  i-j >= j:
					output.append((s,i-j,j))

	return output

total = 0
i = 0
while True:
	i +=1
	total += len(get_triangles(i))
	print i,total
	if total > 10**6:
		break


# for i in range(0,101):
# 	A= get_triangles(i)

# 	S = sum([a[1]/2 for a in A])
# 	print i,A







# def get_triangles(s):
# 	# solves s>  kmn  k,m,n > 0
# 	output = []
# 	for m in range(1,s+1):
#  		for n in range(1,m):
#  			if gcd(m,n)!=1 or (m-n) % 2 ==0:
# 				continue
# 			a = m**2 - n**2
# 			b = 2*m*n
# 			c = m**2 + n**2
# 			maxlen = max(a,b)
# 			if maxlen > s:
# 				break
# 			for k in range(1,s+1):
# 				if k*maxlen > s:
# 					break
# 				output.append((k*a,k*b))
# 	return output

# A = get_triangles(100)
# B = []
# for x,y in A:
# 	for i in range(1,x/2):
# 		B.append((i,x-i,y))
# 	for i in range(1,y/2):
# 		B.append((i,x-i,y))

# C = []
# perfect_squares = set([i**2 for i in range(1,10000)])
# for a,b,c in B:
# 	d1 = (a**2 + (b+c)**2)
# 	d2 = (b**2 + (a+c)**2)
# 	d3 = (c**2 + (a+b)**2)
# 	minlen = min([d1,d2,d3])
# 	if d1 in perfect_squares and d1==minlen:
# 		C.append((a,b,c))

# 	if d2 in perfect_squares and d2==minlen:
# 		C.append((a,b,c))

# 	if d3 in perfect_squares and d3==minlen:
# 		C.append((a,b,c))



# print len(B),len(C)









# # def get_triangles(s):
# # 	# solves s>  kmn  k,m,n > 0
# # 	output = []
# # 	for m in range(1,s):
# #  		for n in range(1,m):
# #  			if gcd(m,n)!=1 or (m-n) % 2 ==0:
# # 				continue
# # 			a = m**2 - n**2
# # 			b = 2*m*n
# # 			c = m**2 + n**2
# # 			maxlen = max(a,b,c)
# # 			if maxlen > s:
# # 				break
# # 			for k in range(1,s):
# # 				if maxlen*k > s:
# # 					break
# # 				output.append((k*a,k*b,k*c))
# # 	return output

# # A = get_triangles(100)

# # total = set()


