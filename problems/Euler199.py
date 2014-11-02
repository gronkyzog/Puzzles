from math import sqrt

def find_r(a,b,c,inner):
	if inner:
		return (a*b+a*c+b*c-2*sqrt(a**2*b*c+a*b**2*c+a*b*c**2))*c*b*a/(a**2*b**2-2*a**2*b*c+a**2*c**2-2*a*b**2*c-2*a*b*c**2+b**2*c**2)
	else:
		return (a*b+a*c-c*b-2*sqrt(a**2*b*c-a*b**2*c-a*b*c**2))*b*c*a/(a**2*b**2-2*a**2*b*c+a**2*c**2+2*a*b**2*c+2*a*b*c**2+b**2*c**2)



def pack_circles(a,b,c,inner,k):
	r = find_r(a,b,c,inner)
	if k==1:
		return r**2
	else:
		if inner:
			return r**2 + pack_circles(a,b,r,True,k-1)+  pack_circles(a,c,r,True,k-1) +pack_circles(b,c,r,True,k-1) 
		else:
			return r**2 + pack_circles(a,b,r,False,k-1)+  pack_circles(a,c,r,False,k-1) +pack_circles(b,c,r,True,k-1) 



k=10
a = 2*(3**0.5)-3
total = 3*a**2
total += pack_circles(a,a,a,True,k)
total += 3*pack_circles(1,a,a,False,k)
total = 1-total
print '%1.8f' % total
