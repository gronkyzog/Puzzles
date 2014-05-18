import itertools


n = 4

counter =0
for X in itertools.permutations(range(1,n+1),n):
	 Y,Z = X[1:],X[:-1]
	 k = sum([1 for y,z in zip(X,Y) if y<z])
	 if k==1:
	 	counter +=1
print counter
