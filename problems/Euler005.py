def gcd(a,b):
    while b != 0:
        a,b = b,a % b
    return a

def gcdArray(A):
	if len(A) ==2:
		return gcd(A[0],A[1])
	elif len(A)>2:
		return gcd(A[0],gcdArray(A[1:]))
	else:
		raise 

def lcm(a,b):
	return (a*b)/gcd(a,b)

def lcmArray(A):
	if len(A) ==2:
		return lcm(A[0],A[1])
	elif len(A)>2:
		return lcm(A[0],lcmArray(A[1:]))
	else:
		raise 

def test():
	n = 20
	X = lcmArray([i for i in range(2,n+1)])
	return X


if __name__ == '__main__':
    print test()



