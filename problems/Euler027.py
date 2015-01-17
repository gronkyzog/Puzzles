import eulertools 


def test():
	P =set(eulertools.primesieve(10000))
	max_counter = 0
	for a in range(-100,1000):
		for b in range(-100,1000):
			x = 0
			while True:
				f = x**2 +a*x + b
				if f not in P:
					break
				x+=1
			if x > max_counter:
				max_counter = x
				#print x,a,b,a*b
				sol = a*b
	return sol


if __name__ == '__main__':
    print test()