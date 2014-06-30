
import numpy
def sequence(n):
	output = [((100003 - 200003*k + 300007*(k**3)) % 1000000) - 500000 for k in range(1,56)]

	if n < 56:
		return output[:n]
	else:
		for k in range(56,n+1):
			output.append(((output[-24] + output[-55] + 1000000) % 1000000) - 500000)

	return output

S = sequence(4000000)
A = numpy.reshape(S,[2000,2000]).T


def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far




def stripe(A,d):
	if A.shape[0] != A.shape[1]:
		raise Exception('Non Square')
	n = A.shape[0]
	
	if d == 'D':
		return [A[a,:] for a in range(0,n)]

	elif d == 'R':
		return [A[:,a] for a in range(0,n)]
	elif d == 'DL':
		return [A.diagonal(offset = a) for a in range(-n+1,n)]
	elif d == 'DR':
		return [A[:,::-1].diagonal(offset = a) for a in range(-n+1,n)]
	else:
		raise Exception('WTF')




	#Returns A stripped in the direction of x,y

#A = numpy.array([[-2,5,3,2],[9,-6,5,1],[3,2,7,3],[-1,8,-4,8]])



#print S[99]
Down = max([max_subarray(b) for b in stripe(A,'D')])
Right= max([max_subarray(b) for b in stripe(A,'R')])
DownLeft = max([max_subarray(b) for b in stripe(A,'DL')])
DownRight = max([max_subarray(b) for b in stripe(A,'DR')])

print Down,Right,DownRight,DownLeft
print max(Down,Right,DownRight,DownLeft)


