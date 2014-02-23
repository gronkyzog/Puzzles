def extract_digits(n,q=10):
	output = []
	r = n
	while r > 0:
		r,s = divmod(r,q)
		output.append(s)
	return output


def terminate(n):
	if n ==0:
		return 0
	x = n
	while True:
		dx = extract_digits(x)
		x = sum([y**2 for y in dx])
		if x in (1,89):
			return x

counter =0


A = [terminate(i) for i in range(0,568+1)]

counter = 0
for x in range(1,10**7):
	dx = extract_digits(x)
	s = sum([d**2 for d in dx])
	if A[s] == 89:
		counter +=1

	if x % 100000==0:
		print x,counter


print x,counter


