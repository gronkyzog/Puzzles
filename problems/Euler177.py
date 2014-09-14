from math import sin,cos,radians,atan2,degrees

C = [cos(radians(t)) for t in range(360)]
S = [sin(radians(t)) for t in range(360)]

def min_sol(w,s,t,x,z,v,u,y):
  r1 = (w,s,t,x,z,v,u,y)
  r2 = (t,x,z,v,u,y,w,s)
  r3 = (z,v,u,y,w,s,t,x)
  r4 = (u,y,w,s,t,x,z,v)

  r5 = (x,t,s,w,y,u,v,z)
  r6 = (s,w,y,u,v,z,x,t)
  r7 = (y,u,v,z,x,t,s,w)
  r8 = (v,z,x,t,s,w,y,u)

  return r1 == min(r1,r2,r3,r4,r5,r6,r7,r8)


def f(w,x,y,z):
  a,b = S[x]/S[w+x], S[w]/S[w+x]
  c,d = S[z]/S[y+z], S[y]/S[y+z]
  s = degrees(atan2(c*S[w+y],a-c*C[w+y]))
  t = 180-w-x-s
  u = 180-w-y-s
  v = 180-y-z-u
  if abs(round(s)-s)<1e-9:
    #return True,(w,x,y,z,int(round(s)),int(round(t)),int(round(u)),int(round(v)))
    return True,(w,int(round(s)),int(round(t)),x,z,int(round(v)),int(round(u)),y)
  else:
    return False,None

counter =0
total = 0
for w in range(1,180):
  for x in range(1,180-w):
    for y in range(1,180-w):
      maxz = min(180-y,180-x)
      for z in range(1,maxz):
        sol,s= f(w,x,y,z)
        if sol:
          if min_sol(*s):
            counter +=1
        total +=1

  print w,total,counter
print counter