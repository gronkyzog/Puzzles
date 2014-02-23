def S(a,b,k):
	if k ==0:
		return a*b
	elif k > 0:
		return 2*(a+b) + 4*(k-1)
	else:
		raise Exception('Negative k %d' %k)


def surface(a,b,c,k):
	return c*S(a,b,k) + 2*sum([S(a,b,s) for  s in range(0,k)])

def layer(a,b,c,k):
	return 2*(2*(k-1)*(a+c)+2*(k-1)*(k+b-2)+a*b+a*c+b*c)


maxsize = 20000
score = [0 for i in range(maxsize+1)]
a = 1
for k in range(1,100):
	for a in range(1,5000):
		if layer(a,a,a,k) > maxsize:
			break
		for b in range(a,5000):
			if layer(a,b,b,k) > maxsize:
				break
			for c in range(b,5000):
				size  =layer(a,b,c,k) 
				if size > maxsize:
					break
				else:
					score[size] +=1

	print a,max(score),[i for i,x in enumerate(score) if x ==1000]

print min([i for i,x in enumerate(score) if x ==1000]) 
