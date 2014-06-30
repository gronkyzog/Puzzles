def generate_digits(n):
	# digits of 1/n
	output = []
	first_rem = {}
	x =1 
	i=0
	while True:
		i+=1
		d,r = divmod(x,n)
		#print d,r
		x = 10*r
		if r not in first_rem:
			first_rem[r] = i
		else:
			return output,i-first_rem[r]
		output.append(d)
		

max_len = 0
for i in range(2,1001):
	digits,cycle_len = generate_digits(i)
	if cycle_len > max_len:
		max_len  = cycle_len
		print i,max_len,digits
