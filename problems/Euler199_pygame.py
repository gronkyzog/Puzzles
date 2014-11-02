import pygame
import sys
from math import sqrt

pygame.init()

screen = pygame.display.set_mode((640,640))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)


def find_r(a,b,c,inner=True):
	if inner:
		return (a*b+a*c+b*c-2*sqrt(a**2*b*c+a*b**2*c+a*b*c**2))*c*b*a/(a**2*b**2-2*a**2*b*c+a**2*c**2-2*a*b**2*c-2*a*b*c**2+b**2*c**2)
	else:
		return (a*b+a*c-c*b-2*sqrt(a**2*b*c-a*b**2*c-a*b*c**2))*b*c*a/(a**2*b**2-2*a**2*b*c+a**2*c**2+2*a*b**2*c+2*a*b*c**2+b**2*c**2)





def draw_circle(x,y,r,colour=(255,255,255)):
	# draws in (-1,-1),(1,1) coordinates
	sx = int(round(320 +320*x))
	sy = int(round(320 -320*y))
	sr = int(round(320*r))
	pygame.draw.circle(screen, colour,(sx,sy) ,sr,3)  





a = 1.
#b = 2*(3**0.5)-3
b=0.2
c = b

s = (a**2-a*b-a*c-b*c)/(a-b)
t = 2*sqrt(a**2*b*c-a*b**2*c-a*b*c**2)/(a-b)

r = (a*b+a*c-c*b+2*sqrt(a**2*b*c-a*b**2*c-a*b*c**2))*b*c*a/(a**2*b**2-2*a**2*b*c+a**2*c**2+2*a*b**2*c+2*a*b*c**2+b**2*c**2)
x = (a**2-a*b-a*r-b*r)/(a-b)
y =  -2*sqrt(a**2*b*r-a*b**2*r-a*b*r**2)/(a-b)
r1,x1,y1 = r,x,y
r = (a*b+a*c-c*b-2*sqrt(a**2*b*c-a*b**2*c-a*b*c**2))*b*c*a/(a**2*b**2-2*a**2*b*c+a**2*c**2+2*a*b**2*c+2*a*b*c**2+b**2*c**2)
x = (a**2-a*b-a*r-b*r)/(a-b)
y =  2*sqrt(a**2*b*r-a*b**2*r-a*b*r**2)/(a-b)
r2,x2,y2 = r,x,y

r3 = find_r(b,c,r1)


draw_circle(0,0,a)
draw_circle(a-b,0,b)
draw_circle(s,t,c)
draw_circle(x1,y1,r1,red)
draw_circle(x2,y2,r2,green)
draw_circle(0,0,r3,blue)
pygame.display.update()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


# import eulertools


# def find_r(a,b,c):

# 	denom= (a**2*b**2-2*a**2*b*c+a**2*c**2-2*a*b**2*c-2*a*b*c**2+b**2*c**2)
# 	A = 1.
# 	B = (-2*a**2*b**2*c-2*a**2*b*c**2-2*a*b**2*c**2)/denom
# 	C = ((a*b*c)**2)/denom

# 	r1 = (-B + (B**2-4*A*C)**0.5)/(2*A)
# 	r2 = (-B - (B**2-4*A*C)**0.5)/(2*A)
# 	if r1>0 and r2>0:
# 		return min(r1,r2)
# 	elif r1>0:
# 		return r1
# 	elif r2>0:
# 		return r2
# 	else:
# 		raise
	
	

# def calc_area(a,b,c,k):
# 	r = find_r(a,b,c)
# 	print k,a,b,c,r
# 	if k ==1:
# 		return r**2
# 	else:
# 		return r**2 + calc_area(a,b,r,k-1)+ calc_area(a,c,r,k-1) + calc_area(b,c,r,k-1)


# covered3 = 1.-0.06790342
# print covered3

# a= (0.25 )*(3**0.5)

# total = 3*a**2
# total += calc_area(a,a,a,3)
# total += 3*calc_area(-1.,a,a,3)

# print total
