import itertools 
import math
def ncr(n,r):
	return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def count(n):
	return ncr(26,n)*(2**n - n -1)


A = [count(n) for n in range(1,27)]	

print max(A)
