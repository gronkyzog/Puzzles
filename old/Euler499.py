import math

def volume(a,b,c):
	# solves volume for elipse with 
	return 4.*math.pi*(a*b*c)/3.

a = 2.
b = 1.

V =  volume(a+1,a+1,b+1) - volume(a,a,b)	


print V
print (V/math.pi)*3./4.
V = 60.35475635
print (V/math.pi)*3./4.