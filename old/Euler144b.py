import math
result = 0
 
xA = 0.0
yA = 10.1
 
xO = 1.4
yO = -9.6
 
while(xO > 0.01 or xO < -0.01 or yO < 0):
    print '%d,%f,%f' %(result,xO,yO)
    #Calculate the slope of A
    slopeA = (yO - yA) / (xO - xA)
 
    #Calculate the slope of the ellipse tangent
    slopeO = -4.*xO/yO
 
    #//Calculate the slope of B
    tanA = (slopeA - slopeO)/(1+slopeA*slopeO)
    slopeB = (slopeO- tanA)/ (1+ tanA*slopeO)
 
    #calculate intercept of line B
    interceptB = yO - slopeB * xO
 
    #solve the quadratic equation for finding
    #the intersection of B and the ellipse
    #a*x^2 + b*x + c = 0
    a = 4 + slopeB*slopeB
    b = 2 * slopeB * interceptB
    c = interceptB * interceptB - 100
 
    ans1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    ans2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
 
    xA = xO
    yA = yO
 
    #Take the solution which is furtherst from x0
    xO = ans1 if (abs(ans1 - xO) > abs(ans2 - xO)) else ans2
    yO = slopeB * xO + interceptB
 
    result +=1
print result