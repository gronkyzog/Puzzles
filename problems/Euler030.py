import time


def extract_digits(x):
	output = []
	r = x 
	while r >0:
		r,k = divmod(r,10)
		output.append(k) 
	return output[::-1]

def cycle(q,n=1):
	if n == 1:
		for a in range(q):
			yield [a]
	else:
		for x in range(q):
			for y in cycle(q,n-1):
				output = [x]
				output.extend(y)
				yield output



def test():
	sumSet = set()
	for x in range(2,1000000):
		digits = extract_digits(x)
		power_sum = sum([s**5 for s in digits])
		if x == power_sum:
			sumSet.add(x)

	return sum(sumSet)


if __name__ == '__main__':
    print test()
	 
