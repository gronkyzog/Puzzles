import itertools

# 0 1
#  4
#  6
#  5
# 2 3
def brute_force(n):
	counter =0
	Q = range(n)
	for x in itertools.product(Q,repeat=7):
		if x[0]== x[1] or x[0]== x[2] or x[2]== x[3] or x[1]== x[3]:
			continue

		if x[0]==x[4] or x[1]==x[4] or x[2]== x[5] or x[3]== x[5]:
			continue 

		if x[4]==x[6] or x[5]==x[6]:
			continue
		else:
			counter +=1

	return counter


for s in range(3,12):
	print '%d,%d' %(s,brute_force(s))