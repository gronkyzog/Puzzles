def f(m,n):			
	output = [0 for i in range(0,n+1)]
	for t in range(0,n+1):
		if t < m:
			output[t] = 1
		else:
			total = 1
			for s in range(m,t+1):
				if (t-s-1)>0:
					total += (s-(m-1))*output[t-s-1]
				else:
					total += (s-(m-1))
			output[t] = total

	return output[-1]

i=50
while True:
	sol = f(50,i)
	if sol > 10**6:
		print i,sol
		break
	i=i+1

