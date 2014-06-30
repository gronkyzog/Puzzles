
import itertools 
def mul(a,b):
	if a is None or b is None:
		return None
	return a*b
def add(a,b):
	if a is None or b is None:
		return None
	return a+b
def sub(a,b):
	if a is None or b is None:
		return None
	return a-b
def div(a,b):
	if a is None or b is None or b ==0:
		return None

	else:
		return a/b

def MaxSequence(A):
	Operators = [add,mul,sub,div]
	output = set()
	for X in itertools.permutations(A):
		for ops in itertools.product(Operators,repeat=3):
			total = ops[0](X[0],X[1])
			total = ops[1](total,X[2])
			total = ops[2](total,X[3])
			err = abs(total - round(total))
			if total > 0 and err < 1e-10:
				output.add(int(total))
			#if total.denominator ==1 and total > 0:
			#	output.add(total.numerator)

			L = ops[0](X[0],X[1])
			R = ops[1](X[2],X[3])
			total = ops[2](L,R)
			err = abs(total - round(total))
			if total > 0 and err < 1e-10:
				output.add(int(total))
			#if total.denominator ==1 and total > 0:
			#	output.add(total.numerator)


	output = list(output)
	output.sort()
	if output[0] != 1:
		return None,None
	n = len(output)
	for i in range(0,n-1):
		if output[i+1] - output[i] > 1:
			return output[i],output



max_s = -1
P = [i for i in range(1,10)]
for A in itertools.combinations(P,4):
	Z = [1.0*a for a in A]
	s = MaxSequence(Z)
	if s[0] > max_s:
		print A,s
		max_s = s[0]
