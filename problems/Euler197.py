

up = -1.
u = int(2**(30.403243784-up**2))*10**(-9)
sumu = up+u

for i in range(10**6):
	u,up = int(2**(30.403243784-u**2))*10**(-9),u
	sumu,sumup = u+up,sumu
	if sumu==sumup:
		#print sumu,sumup
		break

print sumu



