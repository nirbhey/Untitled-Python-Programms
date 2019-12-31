def divideFunction():

    try:

        x = int(input('Enter number x: '))
        y = int(input('Enter number y: '))

        print('x/y = ', x/y)
    except Exception as varToHandle: # IN java this would be "e", good in python you can keep it anything!
        print(varToHandle)
        divideFunction()

divideFunction()