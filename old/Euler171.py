def solve(n):
	mapper = {}
	mapper[0] = [0,1]
	for i in range(n):
		temp = {}
		for k,v in mapper.items():
			for s in range(10):
				ds = k + s**2
				if ds not in temp:
					temp[ds] = [0,0]

				Z = temp[ds]
				Z[0] += 10*v[0] + s*v[1]
				Z[1] += v[1]

		mapper = temp
	return mapper

sol = solve(20)
total = 0
xmax = int(max(sol.keys())**0.5)
for i in range(1,xmax+1):
	x = i**2
	if x in sol:
		total += sol[x][0]
		total = total % 10**9
		print i,x,total



