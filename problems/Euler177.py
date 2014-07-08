from math import sin,cos,radians,atan2,degrees




# counter = 0
# for w in range(1,180):
# 	for x in range(1,180-w):
# 		for y in range(1,180-w):
# 			for z in range(1,min(180-x,180-y)):
# 				if w != x:
# 					a,b = abs(sin(radians(x))/sin(radians(w-x))),abs(sin(radians(w))/sin(radians(w-x)))
# 					print a*sin(cos(w)) - b*sin(cos(x))
# 				counter +=1
# 	print w,counter



counter = 0
for w in range(1,180):
	for x in range(1,180-w):
		if x != w:
			a,b = (sin(radians(x))/sin(radians(w+x))),(sin(radians(w))/sin(radians(w+x)))
			for y in range(1,180-w):
				for z in range(1,min(180-y,180-x)):
					c,d = (sin(radians(z))/sin(radians(y+z))),(sin(radians(y))/sin(radians(y+z)))
					try:
						s = degrees(atan2(a*sin(radians(w+y)),(c-a*cos(radians(w+y)))))
						if abs(round(s)-s)<1e-9:
							counter +=1
					except:
						raise

						#print counter,w,x,y,z,round(s)
	print w,counter
