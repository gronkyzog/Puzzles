n = 4000000

S = [1,2]
next = S[-1] + S[-2]
while next < n:
	S.append(next)
	next = S[-1] + S[-2]

print sum([s for s in S if s%2 ==0])