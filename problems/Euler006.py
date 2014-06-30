def s(n,k):
	return sum([i**k for i in range(1,n+1)])

def test():
	S1 = s(100,1)**2
	S2 = s(100,2)
	return S1-S2

if __name__ == '__main__':
    print test()


