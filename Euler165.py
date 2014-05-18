import itertools

nlines = 5000

s = 290797
points = []
for x in range(nlines+4):
	s = s**2 % 50515093
	t = s % 500
	points.append(t)




lines = [((points[i],points[i+1]),(points[i+2]-points[i],points[i+3]-points[i+1])) for i in range(nlines)]


print lines[4999]





# def Ulam(a,b,n):
# 	output = [a,b]
# 	while len(output)<n:
# 		temp = [x+y for x,y in itertools.combinations(output,2) if (x+y) > output[-1]]
# 		temp.sort()
# 		for x in temp:
# 			if temp.count(x)==1:
# 				output.append(x)
# 				break
# 	return output


# for x in Ulam(2,19,500):
# 	print x
