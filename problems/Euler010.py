import eulertools 

def test():
	return sum(eulertools.primeseive(2000000))

if __name__ == '__main__':
    print test()