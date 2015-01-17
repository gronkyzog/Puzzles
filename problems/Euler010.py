import eulertools 

def test():
	return sum(eulertools.primesieve(2000000))

if __name__ == '__main__':
    print test()