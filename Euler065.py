def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]

def exp_cond_frac(n):
	for i in range(0,n):
 		if i % 3 ==1:
 			yield 2*((i-1)/3 +1)
 		else:
 			yield 1

def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a



h_prev,h_prev_prev = 0,1
k_prev,k_prev_prev = 1,0

i=2
for a in exp_cond_frac(99):
	h = a*h_prev + h_prev_prev
	k = a*k_prev + k_prev_prev
	h_prev,h_prev_prev = h,h_prev
	k_prev,k_prev_prev = k,k_prev
	print i,a,h+2*k,k
	i=i+1

print sum(extract_digits(h+2*k)),gcd(h+2*k,k)




#p