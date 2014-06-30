import numpy

def drs(x):
	r = x
	output = 0
	while r > 0:
		r,q = divmod(r,10)
		output +=q


	if output >= 10:
		return drs(output)
	else:
		return output



n = 10**6
Factors = [[] for i in range(n+1)]
for i in range(2,n+1):
	for j in range(0,n+1,i):
		if i**2 <= j:
			Factors[j].append((i,j/i))


MDRS = [0 for i in range(n+1)]
MDRS[0] = 0
MDRS[1] = 1
MDRS[2] = 2

for i in range(3,n+1):
	F = Factors[i]
	maxsum = drs(i)
	for f in F:
		if MDRS[f[0]] == 0 or MDRS[f[1]] == 0:
			raise Exception('WTF %d %d' %f )
		maxsum = max(maxsum,MDRS[f[0]]+MDRS[f[1]])
	MDRS[i] = maxsum



print sum(MDRS)-MDRS[n]-MDRS[1]-MDRS[0]

