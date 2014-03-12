import numpy
def q150():
    x = numpy.arange(2**20, dtype=numpy.int64)
    x = (615949*x + 797807) % 2**20
    s = numpy.empty(500500+1,dtype=numpy.int64)
    t = 0
    s[0] = 0
    for k in xrange(1,500500+1):
        t = x[t]
        s[k] = t - 2**19
    del x
    print s[1:4]
    r,c = numpy.mgrid[:1000,:1000]
    s = s[numpy.tril(r*(r+1)/2 + c + 1)]
    del r,c
    s0 = s
    best = s.min()
    t = s
    p = numpy.zeros((1001,1001), dtype=numpy.int64)
    for i in xrange(1,1000):
        n = s[:-1,:-1] + numpy.tril(t[1:,:-1]) + t[1:,1:] - numpy.tril(p[2:,1:-1])
        #n = s[:-1,:-1] +t[1:,:-1] + t[1:,1:] - p[2:,1:-1]
        print i,best,t[0,0]
        p,t,s = t,n,s[:-1,:-1]
        best = min(best, t.min())
    print best

q150()