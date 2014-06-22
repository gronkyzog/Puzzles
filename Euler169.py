def binary_array(n):
	q = n
	output = []
	while q >0:
		q,r = divmod(q,2)
		output.insert(0,int(r))
	return tuple(output)

x =10**25
bx= binary_array(x)
I = [i for i,b in enumerate(bx) if b ==1]
I.reverse()
N = len(bx)
A0  = [1 if i >= I[0] else 0 for i in range(N)] 
for k in range(len(I)-1):
	A1 =  [sum([A0[i] for i in range(j+1,N)]) if I[k+1]<= j <= I[k] else 0 for j in range(N)]
	print k,A1
	A0 = list(A1)

print sum(A1)

