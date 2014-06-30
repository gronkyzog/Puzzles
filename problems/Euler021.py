import eulertools
def cycle(A):
	if len(A)==0:
		yield []
	elif len(A) == 1:
		for a in range(A[0]):
			yield [a]
	else:
		X = A[0]
		for x in range(X):
			for y in cycle(A[1:]):
				output = [x]
				output.extend(y)
				yield output

def allfactors(A):
	F = list(set(A))
	N = [A.count(f)+1 for f in F]
	output = []
	for e in cycle(N):
		output.append(eulertools.product([x[0]**x[1] for x in zip(F,e)]))
	return output



def factorbase(P,x):
	output = []
	residule = x
	for p in P:
		if p > x:
			break
		while True:
			temp,r = divmod(residule,p)
			if r!= 0:
				break
			output.append(p)
			residule = temp
	return output


def d(P,x):
	F = factorbase(P,x)
	A = allfactors(F)
	return sum(A) -x 


def test():
	P = eulertools.primeseive(10000)
	sol = 0
	for x in range(2,10001):
		if d(P,d(P,x))==x and x!= d(P,x):
			sol +=x


	return sol
if __name__ == '__main__':
    print test()