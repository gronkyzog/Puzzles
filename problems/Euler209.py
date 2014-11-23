import itertools 


fmap = {}
def f(n):
	# fibonaci wirg starting values (2,1), this is the number of sequences of lenth n+1 which start and end with the same colour.
	# each neighbouring element in the sequence must satisfy Q(n) and Q(n-1) is False.  The loop is of length n+1 as to create a loop of length n.
	if n in fmap:
		return fmap[n]
	if n==0:
		output = 2
		fmap[0] = output
		return output
	elif n==1:
		output = 1
		fmap[1] = output
		return output
	else:
		output = f(n-1)+f(n-2)
		fmap[n] = output
		return output


# we create the map where each element of the truth table must satisft  T(X1) and T(X2) = 0
mapper = {}
for x in itertools.product((False,True),repeat=6):
	w = tuple([x[1],x[2],x[3],x[4],x[5],x[0] != (x[1] and x[2])])
	ix = x[0] + 2*x[1]+4*x[2]+8*x[3]+16*x[4]+32*x[5]
	iw = w[0] + 2*w[1]+4*w[2]+8*w[3]+16*w[4]+32*w[5]
	mapper[ix] = iw

	




total = 1
# find the length of each cycle.l
while len(mapper)>0:
	x,w = mapper.popitem()
	cycle = [x]
	while w in mapper:
		x = mapper.pop(w)
		cycle.append(x)
		w=x

	total *= f(len(cycle))

print total


