def test():
	x = 2**1000
	A = str(x)
	return sum([int(a) for a in A])


if __name__ == '__main__':
    print test()