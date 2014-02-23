def extract_digits(n,q=10):
	output = []
	r = n
	while r > 0:
		r,s = divmod(r,q)
		output.append(s)
	return output[::-1]


threshold = 0.9

x = 0
counter = 0
pr = 0
threshold = 0.99
while pr < threshold:
	x= x+1
	dx = extract_digits(x)
	n = len(dx)
	if n > 1:
		dy = [dx[i] - dx[i-1] for i in range(1,n)]
	else:
		dy = [0]
	if max(dy) >0  and min(dy) < 0:
		counter +=1

	pr = 1.0*counter/x
	
print x
	
