import itertools
def internalpoint(p,rows,cols):
	if 0<=p[0]<=rows and 0<=p[1]<=cols:
		return True
	else:
		return False


def generate_points(rows,cols):
	for r in range(0,rows+cols+1):
		# left = (#, 0)
		# top  = (rows,#)
		# bottom = (0,#)
		# right = (#,cols)
		left = r
		right = r- 2*cols
		bottom = -r
		top = 2*rows -r
		smax = min(left,top)
		smin = max(right,bottom)
		for s in range(smin,smax+1):
			yield (r,s)


def calc_blocks(rows,cols):
	mapper = {}
	for u,v in itertools.combinations(generate_points(rows,cols),2):
		if u[0]== v[0] or u[1]==v[1]:
			continue
		p1 = (0.5*(u[0]+u[1]),0.5*(u[0]-u[1]))
		p2 = (0.5*(v[0]+v[1]),0.5*(v[0]-v[1]))
		p3 = (0.5*(u[0]+v[1]),0.5*(u[0]-v[1]))
		p4 = (0.5*(v[0]+u[1]),0.5*(v[0]-u[1]))
		length = abs(u[0]-v[0])
		height = abs(u[1]-v[1])
		if internalpoint(p1,rows,cols) and  internalpoint(p2,rows,cols) and  internalpoint(p3,rows,cols) and  internalpoint(p4,rows,cols):
			#print length,height,u,v,p1,p2,p3,p4
			key = tuple([length,height])
			if key not in mapper:
				mapper[key]=0
			mapper[key] +=1


	return {k: v/2 for k,v in mapper.items()}


for k,v in calc_blocks(47,43).items():
	print k,v






