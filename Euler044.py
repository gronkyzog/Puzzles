
def genPent(n):
	return [i*(3*i-1)/2 for i in range(1,n+1)]


A = set(genPent(20000))
B = list(A)
B.sort()
for x in B:
	for y in B:
		if y > x:
			break
		if x+y in A and abs(x-y) in A:
			print x,y,abs(x-y)
			