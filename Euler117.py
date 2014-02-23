
def f(n):
	output = [1,1,2,4]
	for s in range(3,n):
		z = output[s-3] + output[s-2] + output[s-1] + output[s]
		output.append(z)


	return output[-1]


print f(50)
