import random
A = [680,319,180,690,129,620,762,689,318,368,710,720,629,168,160,716,731,736,729,316,769,290,719,389,162,289,718,790,890,362,760,380,728]
random.shuffle(A)
print A
A = [str(a) for a in A]

def issequence(A,B):
	C = str(B)
	for a in A:
		i = C.find(a)
		if i == -1:
			return False
		else:
			C = C[i:]
	return True


def all_sequence(A,B):
	for a in A:
		if not issequence(a,B):
			return False
	return True


while True:
	random.shuffle(A)
	total = ''.join(A)
	while True:
		n = len(total)
		exitflag = True
		for i in range(0,n):
			temp = list(total)
			temp.pop(i)
			if all_sequence(A,temp):
				total = temp
				#print temp,len(temp)
				exitflag = False
				break
		if exitflag:
			break
	print ''.join(total)
	if len(total)== 8:
		break
