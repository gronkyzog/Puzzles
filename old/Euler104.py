def extract_digits(x,q=10):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,q)
		output.append(k) 
	return output[::-1]

def ispandigital(A):
	B = list(A)
	B.sort()
	if tuple(B) == (1,2,3,4,5,6,7,8,9):
		return True
	else:
		return False 





hpp = 1
hp = 1
fpp  = 1
fp = 1
q = 10**20
for i in range(3,10**7):
	if i % 10000 ==0:
		print i
	if hp > q and hpp > q:
		hp /= 10
		hpp /= 10
	h = hp + hpp
	f = (fp + fpp) % q  

	hp,hpp = h,hp
	fp,fpp = f,fp

	dh = extract_digits(h)[:9]
	df = extract_digits(f)[-9:]
	if ispandigital(df) and ispandigital(dh):
		print i
		break




	
