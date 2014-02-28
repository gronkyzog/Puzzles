
def count_blocks(rows,cols):
	total = 0
	for r in range(0,rows+cols+1):
		if r <= rows:
			cstart = rows - r
		else:
			cstart = (r - rows)

		if r <= cols:
			cend   = rows+r
		else:
			cend =  rows+2*cols - r

		
		for c in range(cstart,cend):
			if c <= cols:
				wc = rows + c -r 
			else:
				wc = rows+2*cols - c - r
			#print r,c,wc
			for s in range(c+1,cend+1):
				if s <= cols:
					ws = rows + s -r 
				else:
					ws = rows+2*cols - s - r
				#print r,c,wc,ws
				total += min(ws,wc)

	total += rows*cols*(rows+1)*(cols+1)/4
	return total


def count_blocks2(m,n):
     return (-6 + 15*n - 15*n**2 + 6*n**4 + 
      m*(-31 + 46*n - 6*n**2 - 24*n**3) +
      m**2*(15 + 45*n + 30*n**2) + 
      m**3*(10 + 5*n))*(n)*(n+1)/180








total = 0
for r in range(1,43+1):
	for c in range(1,47+1):
		temp = count_blocks(r,c)
		print r,c,temp
		total += temp

print total
print count_blocks2(47,43)














# A = calc_blocks(2,3)


# B = [(v,k) for k,v in A.items()]
# B.sort()

# for b in B:
# 	print b

# print sum(A.values())
# #keys = A.keys()
# # keys.sort()

# # for k in keys:
# # 	print k,A[k]







