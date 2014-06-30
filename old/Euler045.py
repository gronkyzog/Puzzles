# P(n) = 1.5*n^2 - 0.5n - TN = 0
# H(n) = 2*n^2 - n - TN = 0 
# All P(2n-1) = H(n) all odd triagonal numbers are hexagonal
i=144

while True:
	HN = i*(2*i-1)
	pr = (1. + 4*1.5*HN)**0.5
	# only take upper roots 
	pu = int((0.5 + pr)/3.)
	PN = pu*(3*pu-1)/2


	if HN== PN:
		print i,pu,HN
		break
	i +=1
