rows = 12
cols = 9
tiles = rows*cols


def firstvacant(x):
    A =  ([i for i,x in enumerate(x) if x==0])
    if len(A) > 0:
        return min(A)
    else:
        return None

def getpossible(target,current,X,Y):
    occupied = set([i for i,x in enumerate(current) if x==1])
    possible = []
    for x in X[target]:
        if len(occupied.intersection(Y[x]))==0:
            possible.append(x)

    return possible


template = []
template.extend([((r,c),(r,c+1),(r,c+2)) for r in range(rows) for c in range(cols-2)])
template.extend([((r,c),(r+1,c),(r+2,c)) for r in range(rows-2) for c in range(cols)])

template.extend([((r,c),(r+1,c),(r+1,c+1)) for r in range(rows-1) for c in range(cols-1)])
template.extend([((r,c),(r,c+1),(r+1,c+1)) for r in range(rows-1) for c in range(cols-1)])	


template.extend([((r,c+1),(r+1,c),(r+1,c+1)) for r in range(rows-1) for c in range(cols-1)])
template.extend([((r,c),(r,c+1),(r+1,c)) for r in range(rows-1) for c in range(cols-1)])	
template.sort()

Y = {}
for s,x in enumerate(template):
	z0 = x[0][0]*cols + x[0][1]
	z1 = x[1][0]*cols + x[1][1]
	z2 = x[2][0]*cols + x[2][1]
	Y[s] = [z0,z1,z2]



X = {j: set() for j in range(tiles)}
for i in Y:
    for j in Y[i]:
        X[j].add(i)


solutions = {tuple(tiles*[0]) :1}

for i in range(tiles):
    temp = {}
    for s,count in solutions.items():
        if firstvacant(s)==i:
            W = getpossible(i,s,X,Y)
            for w in W:
                z = list(s)
                for y in Y[w]:
                    z[y]=1
                z = tuple(z)
                if z not in temp:
                    temp[z] = 0

                temp[z] += count
        else:
            if s not in temp:
                temp[s] =0
            temp[s] += count
    


    solutions =temp
    print i,len(solutions),sum(solutions.values())





