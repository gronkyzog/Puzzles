result = 0
limit = 100000000
x = 1
y = 1
## the hole in the middle is a square.
# the size of the square must be able to cover the 4 triangles evenly
while(x+y < limit):
    print x,y,limit/(x+y)
    xnew = 3 * x + 4 * y
    ynew = 2 * x + 3 * y
    x = xnew
    y = ynew
    result += limit / (x + y)

print result