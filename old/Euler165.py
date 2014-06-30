import itertools
import numpy
from fractions import Fraction


def get_line_intersection(p0_x,p0_y,p1_x,p1_y,p2_x,p2_y,p3_x,p3_y): 
    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x   
    s2_y = p3_y - p2_y

    det = (-s2_x * s1_y + s1_x * s2_y)
    if det ==0:
    	return False,0,0
    #s = Fraction((-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)), det)
    #t = Fraction(( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)),det)

    s = Fraction(-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y),det)
    t = Fraction( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x),det)

	#s = (1.*(-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)))/det
 	# t = (1.*( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)))/det





    if (0 < s < 1 and 0 < t < 1):
        #Collision detected
        i_x = p0_x + (t * s1_x)
        i_y = p0_y + (t * s1_y)
        return True,i_x,i_y
    return False,None,None







nlines = 5000

s = 290797
points = []
for x in range(4*nlines):
	s = s**2 % 50515093
	t = s % 500
	points.append(t)



lines = [[points[4*i],points[4*i+1],points[4*i+2],points[4*i+3]] for i in range(nlines)]
print lines[0]
solutions = set()
counter = 0
for i,(x,y) in enumerate(itertools.combinations(lines,2)):
	sol,a,b = get_line_intersection(x[0],x[1],x[2],x[3],y[0],y[1],y[2],y[3])
	if sol:
		counter +=1
		solutions.add((a,b))

	if i % 10000==0:
		print i,counter,len(solutions)


print i,counter,len(solutions)
