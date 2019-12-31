def functionOne():
    print('Printed from functionOne')

if __name__ =='__main__': # Make sure you have this if this script is going to be imported, otherwise the following lines will be executed in the loading .py file
    print('Printed from outside any function')