# For any radii x, the value of each corner value can be expressed as a quadratic ax^2 + bx +c. 
# For a given radii, the sum of all corners is also quadratic in x
# Summing over all quadratics <=x gives a cubic in x
# solving for the sequence (1,2,3,4) -> (1,25,101,261) gives the coefficients (16/3,-6,14/3,-3) 

def f(n):
	a = 16
	b = -6*3
	c = 14
	d = -9
	return (a*(n**3) + b*(n**2) + c*(n) + d)/3 

# for a 1001x1001 matrix the radii is 501
def test():
	return f(501)


if __name__ == '__main__':
    print test()