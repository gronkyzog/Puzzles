def s(n,k):
	return sum([i**k for i in range(1,n+1)])


S1 = s(100,1)**2
S2 = s(100,2)

print S1
print S2
print S1-S2