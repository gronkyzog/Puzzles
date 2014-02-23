n = 100
output = [[1 for i in range(10)]]

for i in range(n-1):
	last = output[-1]
	new = [sum(last[:s]) for s in range(1,11)]
	output.append(new)


total = 0
for x in output:
	total += 2*sum(x) - x[0] - x[-1] - 9


print total



