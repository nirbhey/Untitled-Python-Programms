from matplotlib import pyplot as plt
import numpy as np

plt.style.use('ggplot')

x, y = np.loadtxt('exampleForMatplotlib.txt', delimiter = ',', unpack = True) # This unpacking makes x and y(variables) into array data type and not lists.

#x = np.loadtxt('exampleForMatplotlib2.txt')
#y = np.loadtxt('csvExampleFile2.csv')

print(x)
print(y)

plt.plot(x, y, label = 'Line 1')

plt.title('First chart!')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.grid(True, color = 'k')
plt.legend()

plt.show()