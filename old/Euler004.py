

maxz = 0
for i in range(100,999):
	for j in range(i,999):
		z = i*j
		str_z = str(z)
		if str_z[:3] == str_z[::-1][:3]:
			if z > maxz:
				print z,i,j,str_z
				maxz = z

