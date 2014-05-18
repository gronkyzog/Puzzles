from math import log

N = 10**12
q = 10**5


total = 1
prod = []
total = 1
for i in range(q+1):
  if i % 5 != 0 and i%2 !=0:
    total *=i
  prod.append(total)



def power(x):
  global prod,q
  k,m  = divmod(x,q)
  a = pow(prod[q],k,q)
  return (a * prod[m]) % q



p2 = 0
k = N
while k > 0:
  k2 = k / 2
  p2 += k2
  k = k2


p5 = 0
k = N
while k > 0:
  k2 = k / 5
  p5 += k2
  k = k2



N2 = int(log(N) / log(2))
N5 = int(log(N) / log(5))

result = 1
for i in range(N2+1):
  for j in range(N5+1):
    p = 2**i*5**j
    if p > N:
      break
    result *= power(N/p)
    result %= q


print result*pow(2,p2-p5,q) % q



