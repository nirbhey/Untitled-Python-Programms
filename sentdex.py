"""
Types of comments

Comments are of two types

1) #

2) ''''''

"""
print(22 / 7)
print(2 ** 7)

var = 55

print('var = ', var)

# Here, variable can also hold a function.

var = print('Function print!')

# Packing and unpacking of variables!
x, y = (1, 2)

print('X + Y = ', x+y)

i = 9

while i > 0 :
    print(i)
    i -= 1

true = False

while not true: # This is a boolean way of !(not)
    print('This will run because true is False!')
    true = True

# Array list or list.
listOne = [1, 9, 10, 7, 11, 19, 8, 6, 18, 36]

for l in listOne : # Each time the var l will be assigned a value of listOne, it can mapped to the values a range would have, but here listOne is considered
    print(l)

for r in range(1, 11):
    print(r)

b = 0
c = 7

for a in range(b, c):
    if a == 0:
        print('\nb < a && c > a\n')
    else:
        i = 0
    print(b, '<', a, '&&', c, '>', a)

if i > 0:
    print(i)
elif i == 0: # else if statement
    print('elif i = ', i)

def functionOne():
    a = b = c = 50

    a += 100 - b + c

    print(a,' ', b, '', c)

def simpleAdd1(num1, num2):
    num1 = num1 +num2
    print('num1 + num2 is ', num1)

def simpleAdd2(num1, num2):
    num1 = num1 +num2
    print('num1 + num2 is ', num1)
'''
def simpleAdd3(num1, num2, num3):
    num1 = num1 +num2
    print('num1 + num2 is ', num1)

simpleAdd3(num1 = 9, num3 = 9, 9) # This will not work, you can only have it one of two ways!
'''
functionOne()
simpleAdd1(4, 5)
simpleAdd2(num2 = 5, num1 = 22) # Python can assign values by order if done by default, otherwise you can assign by naming the variables, this "simpleAdd2(y = 5, x = 22)" will not work on;y the variable names have to be used!

'''
Functions in python can be used by having multiple variables to be accepted as in constructors.
A feature of default is also available in python, its implementation can be used when we are customizing a specific feature of a function and want the rest of it to be default.
'''

def functionDefault1(var1, var2 = 10): # var2 is default variable!
    print('This is var2', var2)

def functionDefault2(var1, var3, var2 = 0,): # all default and non-default parameters have to be together!
    print('This is var2', var2)

functionDefault1(2)
functionDefault2(2, 3)
functionDefault2(2, 3, var2 = 9)

x = 6

X = x

def changeX1():
    global X  # global variable X, to change X, you have to declare it global!
    print('x = ', x, 'X = ', X)
    X += 10
    xx = x # Local variable
    xx += 10
    print('x = ', x, 'X = ', X, 'xx = ', xx)

print('x = ', x, 'X = ', X)
# Can not do this:- print('x = ', x, 'X = ', X, 'xx = ', xx)

changeX1()

x = 7

def changeX2():
    global X  # global variable X
    xx = x  # Local variable
    print('x = ', x, 'X = ', X, 'xx = ', xx)
    xx += 10
    return xx

xx = changeX2()

print('x = ', x, 'X = ', X, 'xx = ', xx)

print('Input something said by print:\n')
varInput = input()
print('\nYour input is: ', varInput)

z = len(listOne) # To check the length of a list
print('length of listOne: ',z)