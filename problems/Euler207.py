from math import log

def isperfectsquare(x):
	s = int(round(x**0.5))
	return s**2 == x




for k in range(100):
	ps = isperfectsquare(4*k+1)
	t = log((1+ (4*k+1)**0.5)/2,2)
	print k,4*k+1,(4*k+1)**0.5,t,2**t