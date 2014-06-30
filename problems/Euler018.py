
def find_max_path(A):
	if len(A) ==1:
		return [A[0][0]]
	else:
		max_prev_row = find_max_path(A[:-1])
		last_row = A[-1]
		max_row = [max_prev_row[0] + last_row[0]]
		n = len(last_row)
		for i in range(1,n-1):
			max_row.append(max(max_prev_row[i-1],max_prev_row[i])+last_row[i])

		max_row.append(max_prev_row[-1]+last_row[-1])
		return max_row


def test():
	A = [[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20,4,82,47,65],
	[19,1,23,75,3,34],
	[88,2,77,73,7,63,67],
	[99,65,4,28,6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
	[04,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
	return max(find_max_path(A))



if __name__ == '__main__':
    print test()