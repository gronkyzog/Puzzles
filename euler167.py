import itertools


def ulam(a,b):
    yield a
    yield b
    seq = [a,b]
    freq = {a+b:1}
    while True:
        first = min([k for k,v in freq.items() if v==1])
        new = [s+first for s in seq]
        freq = {k:v for k,v in freq.items() if k > first}
        for n in new:
            if n not in freq:
                freq[n]=0
            freq[n] +=1
        yield first
        seq.append(first)




def ulam2(a):
    if a % 2 != 1 or a < 5:
        raise Exception('This only works for odd a>=5')
    yield 2
    yield a
    bigstep = 2*a+2
    seq = [0,2,a]
    while True:
        new = [2+s for s in seq]
        new.extend([bigstep+s for s in seq])
        next = min([s for s in new if new.count(s)==1 and s>seq[-1] and s != 2*bigstep])
        yield next
        seq.append(next)
        seq = [s for s in seq if s > next-bigstep]
    

n =7
F = ulam2(n)

temp = [a for a in itertools.islice(F,2*n+2,3*n+2)]
print temp
masterkey = tuple([a-temp[0] for a in temp])
oldi = 0
for i,a in enumerate(F,start=1):
    temp.pop(0)
    temp.append(a)
    
    key = tuple([s-temp[0] for s in temp])
    if key == masterkey:
        print '%d,%d,%d' %(a,i,i-oldi)
        oldi = i



# 5,32,126
# 7,26,126
# 9,444,1778
# 11,1628,6510
# 13,5906,23662
# 15,80,510
# 17,126960
# 19,380882,1523526
# 21,2097152,8388606