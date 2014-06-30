
def power_mod(a,n,p):
	# I know pow(a,n,p) is a standard python function. I'm putting it here for those who would like to write it in another language.
	residule = n
	temp = a
	total = 1
	while residule > 0:
		residule,r = divmod(residule,2)
		if r == 1:
			total = (total * temp) % p
		temp = (temp**2) % p
	return total

a = 1777
total = a
p = 1855
n = 10**8
for i in range(2,p+1):
	total = power_mod(a,total,n)
print i,total
