import numpy
import math
import eulertools 

def test():
	n = 10001 
	max_size = int(n*math.log(n*math.log(n)))
	A = eulertools.primeseive(max_size)
	return A[n-1]

if __name__ == '__main__':
    print test()