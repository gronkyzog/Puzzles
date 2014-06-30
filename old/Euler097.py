a = 28433
k = 7830457

q = 10**10

ans = pow(2,k,q)
ans = ((a*ans) +1) % q
print ans
print len(str(ans))