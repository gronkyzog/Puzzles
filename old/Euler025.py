import math
a = 0.5*(1+5**0.5)
q = 10
k = 5**(-0.5)
s = 999  
print a
print q
print k
print s
n  =(s*math.log(q) - math.log(k))/math.log(a)
print int(math.ceil(n))
