
throws = []


[throws.append((1,i)) for i in range(1,21)]
[throws.append((2,i)) for i in range(1,21)]
[throws.append((3,i)) for i in range(1,21)]
throws.extend([(1,25),(2,25)])
terminators = [(2,i) for i in range(1,21)]
terminators.append((2,25))


combined = []

for z in terminators:
	combined.append((z,))

for x in throws:
	for z in terminators:
		combined.append((x,z))

for x in throws:
	for y in throws:
		if x <= y:
			for z in terminators:
				combined.append((x,y,z))




filtered = [x for x in combined if sum([s[0]*s[1] for s in x]) < 100]

print len(combined)
print len(filtered)


