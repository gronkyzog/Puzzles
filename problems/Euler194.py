import itertools
import math

# this can be solved using chromatic polynomials
# chromatic polynomials can be used to attack the 4 colour map problem
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


def primitivecount(bottomflag):
	# 0 1
	#  2
	#  3
	#  4
	# 5 6
	output = {}
	for x in itertools.product(range(7),repeat=7):
		if x[0]==x[1] or x[0]==x[2] or x[1]==x[2]:
			continue
		if x[0]==x[5] or x[1]==x[6]:
			continue
		if x[2]==x[3] or x[3]==x[4]:
			continue

		if x[4]==x[5] or x[4]==x[6]:
			continue
		if bottomflag and x[5]== x[6]:
			continue

		sx = set(x)
		key = len(sx)
		if max(sx) >= key:
			continue
		if key not in output:
			output[key] = 0
		output[key] +=1
	return output


def numberblocks(q,bottomflag):
	P= primitivecount(bottomflag)
	# work out the number of networks using 3,4,5,6,7 colours, then boost
	# the each colour up to nCr(q,k) choices for each k.
	total = 0
	for k,v in P.items():
		if k <= q:
			total += v*nCr(q,k)
	return total

N = 1984
a = numberblocks(N,True)
b = numberblocks(N,False)
c = a/(N*(N-1))
d = b/(N*(N-1)) 
q = 10**8

mapper = {}

def cycle(x,y):
	key = (x,y)
	if key in mapper:
		return mapper[key]
	else:
		if x == 0 and y ==1:
			return b
		elif x==1 and y ==0:
			return a
		elif x==0:
			total = d*cycle(x,y-1) % q
			mapper[key] = total
			return total
		elif y==0:
			total = c*cycle(x-1,y) %q 
			mapper[key] = total
			return total
		else:
			total = (c*cycle(x-1,y) + d*cycle(x,y-1)) % q
			mapper[key] = total
			return total


print cycle(25,75)



