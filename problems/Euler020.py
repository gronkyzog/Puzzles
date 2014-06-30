import math

def test():
	X = str(math.factorial(100))
	return sum([int(x) for x in X])


if __name__ == '__main__':
    print test()