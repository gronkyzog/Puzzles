def f(x):
	return (2*(x**3) + 3*(x**2) + x)/6



total = set()
for x in range(1,7072):
	print x
	fx = f(x)
	for y in range(0,x-1):
		z = fx-f(y)
		if z > 10**8:
			continue
		sz = str(z)
		if sz == sz[::-1]:
			total.add(z)
print sum(total)
print 2906969179
