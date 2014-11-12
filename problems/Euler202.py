
from eulertools import gcd,factorise,primeseive
r = 12017639147
r = 1000001
r = 1009

h = (r+3)/2
P = primeseive(int(h**0.5)+1)
F = factorise(P,h)

offset = 3- (h % 3) 

print h,F
counter = 0
for i,c in enumerate(xrange(offset,r,3)):
	x  = h+c
	g = gcd(h,c)
	if g==1:
		counter +=1

	print i,x,counter,c,g

print counter

