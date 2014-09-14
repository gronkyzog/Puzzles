

def test():
	dist = {(i,i,i):1 for i in range(1,10)}
	total = 0
	for i in range(2,41):
		temp = {}
		for k,v in dist.items():
			if k[2] >= 1:
				key = (min(k[0],k[2]-1),k[1],k[2]-1)
				if key not in temp:
			 		temp[key]=0
				temp[key] += v

			if k[2] <=8:
				key = (k[0],max(k[1],k[2]+1),k[2]+1)
				if key not in temp:
			 		temp[key]=0
				temp[key] += v

		dist = temp
		total +=sum([v for k,v in dist.items() if k[0]==0 and k[1]==9])
	return total


if __name__ == '__main__':
    print test()
    #print 126461847755