import eulertools
p=1009
q = 3643

n = p*q
phi = (p-1)*(q-1)

A = [(e,(eulertools.gcd(e-1,p-1)+1)*(eulertools.gcd(e-1,q-1)+1)) for e in range(2,phi) if eulertools.gcd(e,phi)==1 ]
minA = min([a[1] for a in A])

print minA

print sum([a[0] for a in A if a[1]==minA])


