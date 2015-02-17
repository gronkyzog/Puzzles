n = 75*10**6


def generate(a,b,c):
	return [
			(2*c + b - 2*a, 2*c + 2*b - a, 3*c + 2*b - 2*a),
			(2*c + b + 2*a, 2*c + 2*b + a, 3*c + 2*b + 2*a),
			(2*c - 2*b + a, 2*c - b + 2*a, 3*c - 2*b + 2*a)
		   ]


sol = [(2,2,3)]
new_sol = sol
total = 1
for i in xrange(n):
	temp = []
	for x in new_sol:
		for s in set(generate(*x)):
			if not (s[0]<= s[1]<= s[2]):
				raise 
			if sum(s) <= n:
				temp.append(s)

	if len(temp)==0:
		break
	#sol.extend(temp)
	new_sol = temp
	total = total + len(temp)
	if i% 10000==0:
		print i,len(sol),len(new_sol),total

print total



# import itertools