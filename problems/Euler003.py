import eulertools
def test():
    x = 600851475143
    rootx = int(x**0.5)+1
    P = eulertools.primeseive(rootx)
    factors = [p for p in P if x% p ==0]
    return max(factors)


if __name__ == '__main__':
    print test()


