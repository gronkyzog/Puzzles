 
def pentagonal(n): return (n * (3*n-1)) // 2  # the nth pentagonal number is given by (3n^2 - n)/2
 
def generalised_pentagonal(n): # 0, -1, 1, -2, 2
    if n % 2 == 0:
        return pentagonal((n//2) + 1)  # pentagonal(n/2 + 1) if n is even
    else:
        return pentagonal(-(n//2) - 1) # pentagonal(-(n/2 + 1)) if n is odd
 
def termsign(i):
    if i % 4 < 2:
        return 1 # add if i mod 4 is 0 or 1
    else:
        return -1 # subtract otherwise
 
pt = [1]
for n in range (1, 100000+1):
     r, i = 0, 0
     while True:
         k = generalised_pentagonal(i)
         if k > n: 
            break
         r += termsign(i) * pt[n - k]
         i += 1
     pt.append(r % 10**6)
     if r % 10**6 ==0:
     	print len(pt)-1,r
     	break

 


