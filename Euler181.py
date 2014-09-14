nblack = 60
nwhite = 40


solution = {((b,w),(b,w)):1 for b in xrange(0,nblack+1) for w in xrange(0,nwhite+1) if b+w>0}

for i in range(1,101):
	temp = {k:v for k,v in solution.items() if k[0]== (nblack,nwhite)}
	for (k,kmax),v in solution.items():
		for b in range(kmax[0],nblack-k[0]+1):
			wmin = 0 if b > kmax[0] else kmax[1]
			for w in range(wmin,nwhite-k[1]+1):
				if (b,w)>= kmax and (k[0]+b)+(k[1]+w)>=i:
					key = ((k[0]+b,k[1]+w),(b,w))
					if key not in temp:
						temp[key]=0
					temp[key]+=v

	solution = temp
	print i,len(solution),sum([v for k,v in solution.items() if k[0]== (nblack,nwhite)])
