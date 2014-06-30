n = 12000

a, b, c, d = 0,1,  1  , 3  

counter = 0
while (a != 1 or b != 2):
	counter +=1
	k = int((n + b)/d)
	a, b, c, d = c, d, k*c - a, k*d - b
	#print '%d/%d' % (a,b)

print counter-2


