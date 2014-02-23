def f(n):
	if n < 3:
		return 1
	else:
		total = 1
		for s in range(3,n+1):
			total += (s-2)*f(n-s-1)


		return total
		return output[-1]


def sol(n):			
	output = [0 for i in range(0,n+1)]
	for t in range(0,n+1):
		if t < 3:
			output[t] = 1
		else:
			total = 1
			for s in range(3,t+1):
				if (t-s-1)>0:
					total += (s-2)*output[t-s-1]
				else:
					total += (s-2)
			output[t] = total

	return output[-1]



for i in range(1,31):
	print i,f(i)




