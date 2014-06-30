import random
_mrpt_num_trials = 5 # number of bases to test
 

def is_probable_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True

	if n % 2 ==0:
		return False

	# write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
	s = 0
	d = n-1
	while True:
	    quotient, remainder = divmod(d, 2)
	    if remainder == 1:
	        break
	    s += 1
	    d = quotient
	assert(2**s * d == n-1)

	# test the base a to see whether it is a witness for the compositeness of n
	def try_composite(a):
	    if pow(a, d, n) == 1:
	        return False
	    for i in range(s):
	        if pow(a, 2**i * d, n) == n-1:
	            return False
	    return True # n is definitely composite

	for i in range(_mrpt_num_trials):
	    a = random.randrange(2, n)
	    if try_composite(a):
	        return False

	return True # no base tested showed n as composite


def cycle(A,k):
	if k==1:
		for a in A:
			yield [a]
	else:
		for a in A:
			B = [b for b in A if b!=a]
			for x in cycle(B,k-1):
				output = [a]
				output.extend(x)
				yield output

def build_number(x):
	A = x[::-1]
	return sum([a*10**i for i,a in enumerate(A)])



#A = [1,2,3,4]		
Total = []	
for s in range(1,10):
	A = [i for i in range(1,s+1)]
	print s
	for x in cycle(A,s):
		z = build_number(x)
		if is_probable_prime(z):
			print z