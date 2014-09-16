# use Lagrangian Multipliers
# F(X) = P_m(X) + lambda(sum(X)-m)
# d/dl =0 -> sum(X) = m
# d/dx_i =0 ->  + i*P_m(X)/x_i + lambda = 0

# -P_m(X)/lambda  =  x_i/i  = constant
# sum(X)  = c*(m+1)*m/2  = m

# c = 2/(m+1)
# x_i =  2*i/(m+1)

from fractions import Fraction

def product(A):
	total = 1
	for a in A:
		total *=a
	return total
def Pmax(m):
	X = [Fraction(2*i,m+1)**i for i in range(1,m+1)]
	return product(X)


sol = 0
for m in range(2,16):
	P = Pmax(m)
	sol += P.numerator/P.denominator
	print m,sol
