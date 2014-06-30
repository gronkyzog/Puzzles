import numpy
def Champernowne(n):
	output = '.'
	i=1
	while len(output) <= n:
		output += str(i)
		i+=1
	return output
	

D = Champernowne(1000000)


A =[int(D[10**i]) for i in range(1,7)]

print numpy.product(A)



