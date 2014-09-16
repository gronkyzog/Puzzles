import math


from fractions import Fraction
# f = (x/k)**k == exp(k*ln(x/k)) == exp(k*ln(x)- k*ln(k))
# df/dk = (ln(x) - ln(k)-1)*exp(k*ln(x)- k*ln(k))
# df/dk = 0 -> ln(x) = ln(ke)
# x = ke -> k = x/e
def isterminatingfraction(x):
	r = x
	while r% 2==0:
		r = r/2

	while r% 5==0:
		r = r/5
	if r==1:
		return True
	return False

total = 0
for x in range(5,10000+1):
	kpeak = x/math.exp(1)
	kfloor = int(math.floor(kpeak))
	kceil = int(math.ceil(kpeak))
	ffloor,fceil = kfloor*math.log(1.*x/kfloor),kceil*math.log(1.*x/kceil)

	if ffloor > fceil:
		k = kfloor
	else:
		k = kceil

	Y = Fraction(x,k)
	if isterminatingfraction(Y.denominator):
		total -= x
	else:
		total += x


print total

