import math

def test():
	a = 0.5*(1+5**0.5)
	q = 10
	k = 5**(-0.5)
	s = 999  
	n  =(s*math.log(q) - math.log(k))/math.log(a)
	return int(math.ceil(n))


if __name__ == '__main__':
    print test()