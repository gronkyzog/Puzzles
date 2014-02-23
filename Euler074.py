import math
factorials = [math.factorial(i) for i in range(0,10)]


#key = set([367945, 367954])
counter = 0
for x in range(1,10**6):
	z = sum([factorials[int(d)] for d in str(x)])
	if z == 367945 or z ==367954:
		counter +=1
print counter

