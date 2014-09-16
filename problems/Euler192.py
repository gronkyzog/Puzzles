from fractions import Fraction


def aprroximate_root(n,maxdenom):
    introot = int(n**0.5)

    la,lb = 0,1
    ua,ub = 1,1
    ma,mb = la+ua,lb+ub
    while mb <= maxdenom:
        #print la,lb,ua,ub,ma,mb
        if (mb*introot + ma)**2 < (mb**2)*n:
            la,lb = ma,mb
        else:
            ua,ub = ma,mb

        ma,mb = la+ua,lb+ub
    lo = introot+Fraction(la,lb)
    hi = introot+Fraction(ua,ub)
    mp = (lo+hi)/2
    if mp**2 > n:
        return lo
    else:
        return hi
    

sol = 0    

for n in range(2,100001):
    if int(n**0.5)**2 ==n:
        continue
    x = aprroximate_root(n,10**12)
    sol += x.denominator
    if n%1000==0:
        print n,sol
    
print sol
