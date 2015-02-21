from fractions import Fraction

def I(x,k):
	if k<=0:
		return 0
	else:
		if x >= 1:
			return Fraction(1,2) + I(x-1,k-1)
		elif Fraction(1,2) < x < 1:
			return Fraction(1,2) - I(1-x,k-1)
		elif 0 <= x <= Fraction(1,2):
			return I(2*x,k-1)/4 + (x**2)/2
		else:
			return -I(-x,k-1)



lb = Fraction(0,1)
ub = Fraction(1,2)

ylb = Fraction(0,1)
yub = Fraction(1,2)

xpoint = Fraction(1,4)
ypoint = Fraction(1,2)
radius = Fraction(1,4)
for i in range(1,100):
	mp = (lb+ub)/2
	ymp = (ylb+ yub)/2 + (ub-lb)/2
	rmp = (mp- xpoint)**2 + (ymp - ypoint)**2
	if rmp == radius**2:
		break
	elif  rmp < radius**2:
		ub = mp
		yub = ymp
	else:
		lb = mp
		ylb = ymp

	if (ub-lb) < 1e-20:
		break


print mp,ymp

print '%.8f' % (1.*(Fraction(1,4) - I(mp,100)))



