
#
#
# Euler 154
from time import time
st=time()

def nf(n,d):
  ctr = 1
  tot = 0
  while True:
    summ = n/(d**ctr)
    if summ==0:break
    ctr += 1
    tot += summ
  return tot

l2={}
for i in xrange(0,200001):
  l2[i]=nf(i,2)
  #print i, nf(i,2)
  
l5={}
for i in xrange(0,200001):
  l5[i]=nf(i,5)
  #print i, nf(i,2)
  
print l2[200000],len(l2)
print l5[200000],len(l5)

#  The last value in each list is the total # of 2s and 5s in 200000!
#  Subtract 12 from each to find the cutoff between divisor and non-divisor
#  199994-12 = 199982
#  49998-12= 49986

x = 0
summ=0

for x in xrange(66667):  #200000/3+1 
  z = 200000 - (x<<1)
  #print x, z,";",l2[x]*2+l2[z]
  if  ((l5[x]*2+l5[z]) < 49987) and ((l2[x]*2+l2[z]) <199983):summ += 3

print summ
print time()-st	

for x in xrange(0,66667,2):  #200000/3+1
  y = (200000 - x)/2
  if ((l5[x]+l5[y]*2) < 49987) and ((l2[x]+l2[y]*2) <199983) :summ += 3

print summ
print time()-st

# ridiculously slow loop
for x in xrange(66667):  #200000/3+1
  f=(200000-x*3)/2
  for i in xrange(1,f):
    y = x+i
    z = 200000-(x+y)
    if ((l5[x]+l5[y]+l5[z]) < 49987) and ((l2[x]+l2[y]+l2[z]) < 199983) :summ += 6
  x += 1

print summ
print time()-st