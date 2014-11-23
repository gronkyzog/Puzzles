from fractions import Fraction

import eulertools

output = [((0,1),(1,1))]

Nmax = 10**8
counter = 0
for i in xrange(0,Nmax+1):
    temp = []
    for lb,ub in output:
        md = (lb[0]+ub[0],lb[1]+ub[1])
        mp = (lb[0]*ub[1] + ub[0]*lb[1],2*lb[1]*ub[1])
        if eulertools.gcd(mp[0],mp[1])!=1:
            raise
        if md[1] <= Nmax:
            if mp[1] <= Nmax:
                if 100*mp[0] < mp[1]:
                    counter += 1

                if 100*lb[0] < lb[1]:
                    temp.append((lb,md))

                if 100*md[0] < md[1]:
                    temp.append((md,ub))

    if len(temp) == 0:
        break
    output = temp
    if i% 100000==0:
        print i,counter
print counter,len(output)









# # def farey( n,peak, asc=True ):
# #     """Python function to print the nth Farey sequence, either ascending or descending."""
# #     if asc: 
# #         a, b, c, d = 0, 1,  1  , n     # (*)
# #     else:
# #         a, b, c, d = 1, 1, n-1 , n     # (*)
# #     yield  Fraction(a,b)
# #     while (asc and c <= n) or (not asc and a > 0):
# #         k = int((n + b)/d)
# #         a, b, c, d = c, d, k*c - a, k*d - b
# #         if peak*a <= b:
# #     		yield Fraction(a,b)
# #     	else:
# #     		break

# # peak = 100
# # maxQ = 10**5
# # solution = set()
# # for q in range(2,maxQ/2+1):
# # 	A = [a for a in farey(q,peak)]
# # 	n = len(A)
# # 	#B = [(A[i],A[i+1],(A[i]+A[i+1])/2) for i in range(n-1)]
# # 	B = [(A[i]+A[i+1])/2 for i in range(n-1)]
	
# # 	C = [b for b in B if b.denominator <= maxQ]
# # 	D = [c for c in C if c not in solution]
# # 	solution.update(C)
# # 	print q,n,len(D),len(solution),[str(d) for d in D]



# # solution = list(solution)
# # solution.sort()

# # for x in solution:
# # 	print x

# outo















# def aprroximate_fraction(n,maxdenom):
#     lo = Fraction(0,1)
#     hi = Fraction(1,1)
#     md = Fraction(lo.numerator+hi.numerator,lo.denominator+hi.denominator)
#     while md.denominator <= maxdenom:
#     	if md < n:
#     		lo = md
#     	else:
#     		hi = md

#     	md = Fraction(lo.numerator+hi.numerator,lo.denominator+hi.denominator)


#     return lo,hi


# print aprroximate_fraction(Fraction(9,40),7)






# # a/b  < c/d  < e/f:

# # mediant  (a+e)/(b+f) = average  (af + eb)/(2bf) 
# # gcd(af+eb,2bf) = gcd(af+eb,2b)*gcd(af+eb,f)  = gcd(af,2b)*gcd(eb,f)
# from fractions import Fraction
# import eulertools

# def farey( n, asc=True ):
#     """Python function to print the nth Farey sequence, either ascending or descending."""
#     if asc: 
#         a, b, c, d = 0, 1,  1  , n     # (*)
#     else:
#         a, b, c, d = 1, 1, n-1 , n     # (*)
#     yield  Fraction(a,b)
#     while (asc and c <= n) or (not asc and a > 0):
#         k = int((n + b)/d)
#         a, b, c, d = c, d, k*c - a, k*d - b
#     	x = Fraction(a,b)
#     	yield x


# solution = set()
# for q in range(1,101):
# 	A = [a for a in farey(q)]
# 	n = len(A)
# 	temp = [(A[i]+A[i+1])/2 for i in range(n-1)]
# 	temp = [a for a in temp if a.denominator == 40]
# 	if len(temp)> 0:
# 		solution.update(temp)
# 		print q,min([a.denominator for a in temp]),len(temp),len(solution)
	

# solution = list(solution)
# solution.sort()

# for x in solution:
# 	print x




# # counter =0
# # ap = Fraction(1,10**5+1)
# # for i,a in enumerate(farey(10**5),start=0):
# # 	if a.numerator*100 > a.denominator:
# # 		break
# # 	else:

# # 		mp = (a + ap)/2
# # 		if mp.denominator <= 10**8:
# # 			counter +=1
# # 			#print ap,a,mp,i,counter 
# # 		ap = a

# # 	if i%10000==0:
# # 		print i,counter,1.*a

# # print counter




# # A = [a for a in farey(10**4)]
# # n = len(A)
# # print n
# # for i in range(n-2):
# # 	lb = A[i]
# # 	md = A[i+1]
# # 	ub = A[i+2]
# # 	mp = (lb+ub)/2
# # 	if mp == Fraction(5,12):
# # 		print lb,ub,mp,md   
# # 		break



# # def midpoint(lhs, rhs):
# #     """ Midpoint of lhs and rhs """
# #     return (lhs[0]*rhs[1] + lhs[1]*rhs[0], 2*lhs[1]*rhs[1])
 
# # def solve(r, D):
# #     """ Find ambiguous rationals
 
# #     Find ambiguous p/q with:
# #     1. p/q < 1/r (i.e. r*p < q)
# #     2. q <= D
# #     """
# #     seq = [(0,1), (1,1)] # F_1, the first Farey sequence
# #     den = 1
# #     ret = r < 2 and 1 or 0 # if 1/2 is included or not
# #     while den < D:
# #         # loop invariant: seq is the Farey sequence F_{den}
# #         # at least up to 1/r
 
# #         idx = 0 # our location in F_den
# #         # iterate to the end of F_den or until seq[idx] > 1/r
# #         while idx < len(seq)-1 and r*seq[idx][0] < seq[idx][1]:
# #             nextidx = idx + 1
# #             mediantden = seq[idx][1] + seq[idx+1][1]
# #             if(mediantden == den + 1): # new element of F_{den+1}
# #                 mediant = (seq[idx][0]+seq[idx+1][0],mediantden)
# #                 seq.insert(idx + 1, mediant)
# #                 nextidx = idx + 2
# #                 # possible new ambiguous numbers
# #                 midleft = midpoint(seq[idx], mediant)
# #                 midright = midpoint(mediant,seq[idx+2])
# #                 if r*midleft[0] < midleft[1] and midleft[1] <= D:
# #                 	print midleft
# #                 	ret += 1
# #                 if r*midright[0] < midright[1] and midright[1] <= D:
# #                     print midright
# #                     ret += 1
# #             idx = nextidx
# #         den += 1
# #     return ret

# # print solve(100, 200)