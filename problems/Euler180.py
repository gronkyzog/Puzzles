from fractions import Fraction
import itertools

def f(n,x,y,z):
	# due to Fermat's last theorem only n in (-2,-1,1,2) will yield zero for x,y,z <> 0
	return (x+y+z)*(x**n + y**n - z**n)


A = set([Fraction(a,b) for b in range(1,36) for a in range(1,b)])


counter = 0
solution = set()
for n in range(-2,3):
	AN = {a**n:a for a in A}
	for x,y in itertools.combinations_with_replacement(A,2):
		zn = x**n + y**n
		if zn in AN:
			z = AN[zn]
			solution.add(x+y+z)

print len(solution)
total = sum(solution)
print total.numerator+total.denominator

