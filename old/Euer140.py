


primitiveset = set()
for x in range(-44,44):
	for y in range(-44,44):
		if x**2 - 5*y**2 == 44:
			primitiveset.add((x,y))
		


for u in range(2,44):
	for v in range(0,44):
		if u**2 - 5*v**2 == 1:
			print u,v
			break


		



# #(u + sv)(9 + 4s)
# #(9u + 20*v,4u + 9v

sol = set()
while len(primitiveset)>0:
	u0,v0 = 9,4
	u,v = u0,v0
	x0,y0 = primitiveset.pop()
	x,y = x0,y0
	for i in range(1000):
		if (x-7) % 5 ==0 and x>0 and y >0 :
			sol.add(((x-7)/5,y))
		#print u,v,u**2 - 5*v**2,x,y,x**2 - 5*y**2
		u,v = 9*u + 20*v,4*u+9*v
		x,y = x0*u + 5*y0*v,y0*u + x0*v



sol = list(sol)
sol.sort()
print sum([x[0] for x in sol[1:31]])
