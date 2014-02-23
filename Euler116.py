

# combinations of partition of length n with blocksize k
def f(n,k):
	output = [1 for i in range(k)]
	for s in range(k,n+1):
		z = output[s-1] + output[s-k]
		output.append(z)


	return output[-1]-1



print f(50,2)+f(50,3)+f(50,4)



# 000  <- 4
# 100  <- 3
# 110  <- 2
# 111  <- 