n = 10**6
a, b, c, d = 1, 1, 3 , 7     
k = int((n + b)/d)
a, b, c, d = c, d, k*c - a, k*d - b
#print "%d/%d  %d/%d" % (a,b,c,d)
print c
#428570/999998