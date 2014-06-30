import itertools

def partition(A):
	n = len(A)
	if n==0:
		yield []
	for i in range(1,n+1):
		L = A[:i]
		R = A[i:]
		for seq in partition(R):
			seq.insert(0,L)
			yield seq




def run():
	for X in itertools.permutations('9876543210'):
		z = ''.join(X)
		print z
		for i,seq in enumerate(partition(z)):
			iseq = [int(s) for s in seq]
			for k in range(2,33):
				if k % 11 ==0:
					continue
				res = [s % k for s in iseq]
				if max(res)==0:
					divisors = [(d/k) for d in iseq]
					divisors.insert(0,k)
					str_divisors = ''.join([str(d) for d in divisors])
					freq = [str_divisors.count(str(s)) for s in range(10)]
					if min(freq)==max(freq)==1:
						print z,seq,k,freq,divisors
						return z

sol = run()
print 'Solution:' + sol




# for i,X in enumerate(itertools.permutations([9,8,7,6,5,4,3,2,1,0])):
# 	z = ''.join([str(x) for x in X])
# 	z = '9857164023'
# 	for seq in partition(z):
# 		for k in range(2,10):
# 			res = [int(s) % k for s in seq]
# 			if max(res)==0:
# 				print z,seq,k,res
# 				divisors = [int(s)/k for s in seq]
# 				divisors.append(k)
# 				divisors = ''.join([str(d) for d in divisors])
# 				freq = [divisors.count(str(d)) for d in range(10)]
# 				if max(freq)==1:
# 					print z,divisors



# def find_sequence(a,data):
# 	seq = []
# 	for s in range(1,len(a)):
# 		z = a[:s]
# 		if z in data:
# 			w = a[:s]
# 			if len(w)==0:
# 				yield [w],''
# 			else:
# 				temp,r =find_sequence(w,data)
# 				temp.append(w)
# 				if len(r)==0:
# 					yield temp,''
# 	yield [],a

			

# mapper = set()
# for s in range(1,11):
# 	print s
# 	for X in itertools.permutations(range(10),s):
# 		z = sum([x*10**(i) for i,x in enumerate(X)])
# 		mapper.add(z)


# mapper2 = {}
# for x in mapper:
# 	for k in range(2,10):
# 		z = k*x
# 		if z in mapper:
# 			if k not in mapper2:
# 				mapper2[k] = set()
# 			mapper2[k].add(str(z))

# A = [str(x) for x in mapper if len(str(x))==10]
# A.reverse()
# print 'Starting'
# for a in A:
# 	print a,type(a)
# 	for k in range(2,10):
# 		seq,r = find_sequence(a,mapper2[k])
# 		if len(r)==0:
# 			print a,seq

			 


# # def partition(A):
# # 	n = len(A)
# # 	for i in range(1,n+1):
# # 		if i==n:
# # 			yield [A]
# # 		else:
# # 			for x in partition(A[i:]):
# # 				y = list(x)
# # 				y.insert(0,A[:i])
# # 				yield y

# # counter = 0
# # for s in range(1,10):
# # 	print s
# # 	A = [range(10-i) for i in range(s)]	
# # 	for X in itertools.product(*A):
# # 		if X[0]==0:
# # 			continue
# # 		Y = range(10)
# # 		Y.reverse()
# # 		z = int(''.join([str(Y.pop(x)) for x in X]))
# # 		for k in range(2,10):
# # 			w = str(k*z)
# # 			if max([w.count(str(i)) for i in range(10)])==1 and str(k) not in str(z):
# # 				counter +=1
# # 				if counter % 1000==0:
# # 					print s,counter

# # print counter,s,k,z,w



# A = [range(10-i) for i in range(10)]
# for i,X in enumerate(itertools.product(*A),start=1):
# 	Y = range(10)
# 	Y.reverse()
# 	Z = [Y.pop(s) for s in X]
# 	for W in partition(Z):
# 		print Z,W










# def partition(n):
# 	if n==0:
# 		yield list([])
# 	if n > 0:
# 		for i in range(1,n+1):
# 			for x in partition(n-i):
# 				temp = list(x)
# 				temp.append(i)
# 				yield temp




# for i,x in enumerate(partition(10),start=1):
# 	print i,x,sum(x)




# # A = [range(10-i) for i in range(10)]
# # for i,x in enumerate(itertools.product(*A)):
# # 	y = range(10)
# # 	y.reverse()
	
# # 	mult = y.pop(0)
# # 	for k in range(9):
# # 		x1 = y[:k]
# # 		x2 = y[k:]
		
# # 	if i % 10000==0:
# # 		print i,mult,x1,x2


# 	