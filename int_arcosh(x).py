import math

def arcosh(x, eps):
    if (x<1): #return false if argument doesn't belong to the domain
        return False
    fsum = math.log(2*x) #define variable fsum by value ln(2x) which is in Taylor series of this function
    i = 1 #auxiliary variable -> next words of the series are build by multiplaying the
                                #numerator by consecutive odd numbers
                                #then i += 2
                                #the denominator increases in direct proportion to the square of
                                #next odd numbers multiplay by x^2
    word = i/(2*i * 2*i * x**2) #first word value
    while (abs(word) > eps): #check if word value is still bigger than expected precision
        i += 2
        fsum -= word #substract word from fsum
        word *= i/(x**2 * i**2) #creationg of next word
    return fsum

def int_arcosh(a, b, n, eps):
    integral = 0
    step = (b-a)/n #our step
    while(a <= b): #split point cannot be bigger than b
        y1 = arcosh(a, eps)
        a += step #add step
        y2 = arcosh(a, eps)
        if(y1 == False or y2 == False):
            return "Part of the range is outside the domain D: x>1"
        integral += (y1 + y2)/2 * step
    return integral

#egazample of use

a = float(input('Enter beginning of interval: '))
b = float(input('Enter end of interval: '))
n = float(input('Enter number of split points: '))
eps = float(input('Enter precision arcosh: '))

result = int_arcosh(a, b, n, eps)
print('int_{' + str(a) + '}^{' + str(b) + '}(arcosh(x)dx) = ' + str(result))
