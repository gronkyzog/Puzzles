def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]


def freq_digits(x):
	Z= extract_digits(x)
	return tuple([Z.count(i) for i in range(0,10)])



freq_map = {}
min_x = 10**9
for x in xrange(0,10**8):
	z = x**3
	f = freq_digits(z)
	if f not in freq_map:
		freq_map[f] = []
	freq_map[f].append(x)
	if len(freq_map[f]) >= 5:
		mx = min(freq_map[f])
		if mx < min_x:
			print len(freq_map),freq_map[f],mx**3
			min_x = mx
			break

		


