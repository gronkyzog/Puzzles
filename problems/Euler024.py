import math

def f(A,x):
	output = []
	R = list(A)
	r = x
	for i in xrange(len(A)-1,0,-1):
		q = math.factorial(i)
		k,r = divmod(r,q)

		output.append(R.pop(k))

	output.append(R.pop())
	return output


def test():
	A = [0,1,2,3,4,5,6,7,8,9]
	x = 999999
	return ''.join([str(s) for s in f(A,x)])


if __name__ == '__main__':
    print test()