b=15    #num in box of chocolates
print(b)

#dif way to get 15 output
def cadbury(a):
    cadbury = a+10
    print (cadbury)
    
cadbury(5)

#another way
cadbury2 = 5
cadburyBox = cadbury2 + 10
print (cadburyBox)

#add to box
print(b+5)
cadbury(10)
print(cadburyBox+5)

cad1='milk chocolate'
cad2='dark chocolate'
cad3='white chocolate'
print('I have three flavors of chocolate:',cad1,',', cad2, ', and', cad3)

name=input('please enter your name:   ')
print('Hello', name)

age = input('Please enter your age:     ')
print('You are', age, 'years old.')

import math
dir(math)

math.pi

math.factorial(0)
math.pow(6 ,2)


def cRoot(a):
    cRoot=math.pow(a,1/3)
    print('the cube root of', a , 'is', cRoot)
cRoot(int(input('What number do you want to find the cubic root of?     ')))