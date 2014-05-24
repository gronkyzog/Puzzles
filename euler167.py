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
    

def generate_ulam_sequence(a):
    F = ulam2(a)
    seq = []
    bigstep = 2*a + 2
    temp = None
    for i,x in enumerate(F):
        seq.append(x)
        if i == 2*bigstep+1:
            masterkey = tuple([s- seq[-a] for s in seq[-a:]])
            temp = seq[-a:]
            i_start = i
            x_start = x

        if temp != None:
            temp.pop(0)
            temp.append(x)
            key = tuple([s - temp[0] for s in temp])

            if key == masterkey:
                return seq,i-i_start,x-x_start

            #print key,masterkey





k = 10**11



total = 0
for s in range(5,23,2):
    seq,freq,diff = generate_ulam_sequence(s)
    q,r = divmod(k,freq)
    if r <= 2*s+2:
        r += freq
        q = q-1
    total += seq[r-1] + q*diff
    #seq2 = [a for a in itertools.islice(ulam2(s),k)]
    print s,len(seq),freq,diff,total,q,r

print total

# 5,32,126
# 7,26,126
# 9,444,1778
# 11,1628,6510
# 13,5906,23662
# 15,80,510
# 17,126960
# 19,380882,1523526
# 21,2097152,8388606