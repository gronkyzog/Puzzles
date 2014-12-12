import sys
import eulertools
import datetime



def shortest_length(P,x):
	# the solution works by factorising the number of solutions into primes.
	# for a given even number, the number of solutions is (product(2*e(i)+1)-1/2) where e(i)
	# is the exponent of the ith prime factorisation
	n = 2*x + 1
	A = eulertools.factorise(P,n)
	A.sort(reverse=True)
	B = [(a-1)/2 for a in A]
	X = P[:len(B)]
	return 2*eulertools.product([x**b for x,b in zip(X,B)])


def test():
	P = eulertools.primesieve(100)
	solution = shortest_length(P,47547)
	return solution


if __name__ == '__main__':
    print test()