import random

listx = []

x = int(input('Enter the value up to which random numbers should go?\n'))

for i in range(x):
    y = random.randrange(-x, x)
    listx.append(y)

print(listx)
print(listx.__len__())

for i in range(100):
    z = random.randrange(21, 25)
    print(z)