def combinations(n):
	# 20 combinations outside pair
	# 30 on inner pairs
	# 5 in central if odd
	# some odds have no solutions
	if n < 2:
		return 0
	elif n%2 ==0:
		k = n/2 -1
		return 20*(30**k)

	elif n==3:
		return 20*5
	elif n==7:
		return 20*30*30*5

	elif n in (5,9):
		return 0

total = 0
for k in range(2,10):
	temp = combinations(k)
	total += temp
	print k,temp,total

