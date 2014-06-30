import math

def test():
	n = 20
	paths = math.factorial(2*n)/(math.factorial(n)**2)
	return paths

if __name__ == '__main__':
    print test()