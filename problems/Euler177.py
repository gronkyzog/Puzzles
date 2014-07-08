from math import sin,cos,radians,atan2,degrees



C = [cos(radians(t)) for t in range(360)]
S = [sin(radians(t)) for t in range(360)]

def f(w,x,y,z):
	a,b = S[x]/S[w+x], S[w]/S[w+x]
	c,d = S[z]/S[y+z], S[y]/S[y+z]
	s = degrees(atan2(a*S[w+y],c-a*C[w+y]))
	return s,abs(round(s)-s)<1e-9


counter =01
for w in range(1,180):
	for x in range(1,180-w):
		for y in range(1,180-w):
			maxz = min(180-y,180-x)
			for z in range(1,maxz):
				s,sol = f(w,x,y,z)
				if sol:
					counter +=1

	print w,counter
print counter

#counter = 01
#for w in range(1,180):
	# for x in range(1,180-w):
	# 	if x != w:
	# 		a,b = (sin(radians(x))/sin(radians(w+x))),(sin(radians(w))/sin(radians(w+x)))
	# 		for y in range(1,180-w):
	# 			for z in range(1,min(180-y,180-x)):
	# 				if w <= y and w+y <= 90:
	# 					c,d = (sin(radians(z))/sin(radians(y+z))),(sin(radians(y))/sin(radians(y+z)))
	# 					s = degrees(atan2(a*sin(radians(w+y)),(c-a*cos(radians(w+y)))))
	# 					if abs(round(s)-s)<1e-9:
	# 						print w,x,y,z
	# 						counter +=1
	# 					else:
	# 						print w,x,y,z

	# print w,counter
