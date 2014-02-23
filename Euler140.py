

def PQA(D,U0,V0):
	rD = D**0.5
	a = int(rD)
	U,V = U0,V0
	Xpp,Xp = -U,V
	Ypp,Yp = 1,0
	Ppp,Pp = 0,1
	i=1
	counter = 0
	while True:
		a = int((U +rD)/V )
		U = a*V - U
		V = (D-U**2)/V
		X = a*Xp + Xpp
		Y = a*Yp + Ypp
		P = a*Pp + Ppp

		Xp,Xpp = X,Xp
		Yp,Ypp = Y,Yp
		Pp,Ppp = P,Pp
		f=  X**2 - D*Y**2
		#print U,V,a,X,Y,f

		if abs(V) == 1:
			return V,X,Y,




print PQA(13,12,12)

#print x,y,x**2 - 5*y**2
