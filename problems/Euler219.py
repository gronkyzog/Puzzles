sol = {0:1}
residual = 10**9 -1
while residual > 0:
	minx = min(sol.keys())
	n_minx = sol[minx]

	if residual >= n_minx:
		sol[minx+1] = sol.setdefault(minx+1,0)+n_minx
		sol[minx+4] = sol.setdefault(minx+4,0)+n_minx
		del sol[minx]		
		residual -= n_minx
	else:
		sol[minx+1] = sol.setdefault(minx+1,0)+residual
		sol[minx+4] = sol.setdefault(minx+4,0)+residual
		sol[minx] -=residual
		residual -= residual
	print residual,n_minx,sum([k*v for k,v in sol.items()])


print sum([k*v for k,v in sol.items()])



# for i in xrange(2,10**9+1):
# 	minx = min(sol.keys())
# 	if sol[minx] ==1:
# 		sol[minx+1] = sol.setdefault(minx+1,0)+1
# 		sol[minx+4] = sol.setdefault(minx+4,0)+1
# 		del sol[minx]


# 	elif sol[minx] >1:
# 		sol[minx+1] = sol.setdefault(minx+1,0)+1
# 		sol[minx+4] = sol.setdefault(minx+4,0)+1
# 		sol[minx] -=1



# 	else:
# 		raise Exception('Broken')

# 	if i % 10**6 ==0:
# 		print '%d,%d,%d,%d' %(i,len(sol),minx,sum([k*v for k,v in sol.items()]))

# print '%d,%d,%d,%d' %(i,len(sol),minx,sum([k*v for k,v in sol.items()]))	

