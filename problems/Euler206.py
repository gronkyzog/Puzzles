

partial = '1_2_3_4_5_6_7_8_9_0'
 

def partial_match(A,B):
	if len(A)!= len(B):
		return False
	for a,b in zip(A,B):
		if a== '_' or b == '_':
			continue
		elif a!=b:
			return False
	return True



output = [0]
for k in range(1,len(partial)+1):
	par_tail = partial[-k:]
	temp = []
	for q in range(10):
		for s in output:
			x = q*10**k + s
			sx = str(x**2)
			if len(sx) <= len(partial):
				sol_tail = sx[-k:]
				if partial_match(sol_tail,par_tail):
					temp.append(x)	

	output = temp
	print k,len(output)
print output[0]
print output[0]**2
print partial