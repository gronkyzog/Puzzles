
import numpy

fp = open('Euler096.txt','r')


def validate(A):
	# sum (1..9)=45 and product (1..9)= 362880
	# if prod and sum check then all must be present and only once
	for i in range(9):
		if numpy.sum(A[i,:]) != 45 or numpy.product(A[i,:]) != 362880:
			return False

	for i in range(9):
		if numpy.sum(A[:,i]) != 45 or numpy.product(A[:,i]) != 362880:
			return False

	for i in range(3):
		for j in range(3):
			if numpy.sum(A[3*i:3*i+3,3*j:3*j+3]) != 45 or numpy.product(A[3*i:3*i+3,3*j:3*j+3]) != 362880:
				return False			
	return True

def get_possible(A,i,j):
	if A[i,j] != 0:
		return set([A[i,j]])
	C = set([s for s in range(1,10) if s not in set(A[i,:])])
	R = set([s for s in range(1,10) if s not in set(A[:,j])]) 
	x,_ = divmod(i,3)
	y,_ = divmod(j,3)
	B = set([s for s in range(1,10) if s not in set(A[3*x:3*x+3,3*y:3*y+3].flatten())]) 
	combined = C.intersection(R).intersection(B)
	return combined

def elimination(A):
	possible = [[get_possible(A,i,j) for j in range(9)] for i in range(9)]
	return possible 

def populate(A):
	while True:
		exitflag= True
		#all_possible = elimination(A)
		for i in range(9):
			for j in range(9):
				if A[i,j] != 0:
					continue
				possible = get_possible(A,i,j)
				#possible = all_possible[i][j]
				if len(possible)==1:
					A[i,j]=possible.pop()
					exitflag = False
		if exitflag:
			return A,validate(A)


def brute_force(A,k=0):
	A,complete = populate(A)
	if complete:
		return A,True
	max_possible = 9
	max_i,max_j = 0,0
	for i in range(9):
		for j in range(9):
			if A[i,j] != 0:
				continue
			possible = get_possible(A,i,j)
			npossible = len(possible)
			if npossible ==0:
				return A,False

			elif npossible < max_possible:
				max_possible = npossible
				max_i,max_j = i,j 


	possible = get_possible(A,max_i,max_j)
	npossible = len(possible)
	#print k,max_i,max_j,npossible,possible
	for p in possible:
		B = 1*A
		B[max_i,max_j]=p
		C,complete = brute_force(B,k+1)
		if complete:
			return C,complete

	return A,validate(A)



data = [x.strip() for x in fp.readlines()]
puzzles = {}
while len(data) >0:
 	name = data.pop(0)
 	A = numpy.array([[int(s) for s in data.pop(0)] for i in range(9)])
 	puzzles[name] = A

total = 0
for k,A in puzzles.items():
	A,complete = brute_force(A)
	total += A[0,0]*100 + A[0,1]*10+A[0,2]
	print k,complete,total

# A = puzzles['Grid 01']
# A,complete = populate(A)
# print A
# print complete