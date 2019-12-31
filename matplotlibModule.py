from matplotlib import pyplot as plt # plt is a common name for pyplot.
#import matplotlib.pyplot as plt # This is another good way to import

# plt.style.use('fivethirtyeight')

plt.style.use('ggplot')

x = [1, 9, 18, 35]
y = [1, 19, 19, 36]

print(x) # Use this for debugging
print(y) # i.e. when you get value errors.
plt.figure("Write_figure_name_here!")
plt.bar([1, 10, 3, 5], [51, 61, 20, 62], color = 'w', label = 'bar 1', width = 1, align = 'center') # Bar graphs.
plt.bar([1, 3, 5, 7], [6, 7, 2, 6], color = 'k', label = 'bar 2', width = 1, align = 'center')

plt.plot(x, y, 'c', linewidth = 5) # plt.plot([x1, x2, x3, x4], [y1, y2, y3, y4])
plt.plot([1, 9, 18, 5], [1, 19, 1, 56], 'yellow', linewidth = 10, label = 'Line 1')# In lines color = '' is not used but is used everywhere else.
plt.plot([1, 9, 8, 35], [1, 19, 9, 3], label = 'Line 2')
plt.plot([1, 9, 18, 5], [1, 1, 19, 2], 'g', linewidth = 1, label = 'Line 3')

plt.scatter([10, 79, 18, 5], [1, 61, 1, 9], color = 'blue', label = 'Scatter 1') # scatter plots are points of data.
plt.scatter([1, 9, 58, 51], [12, 1, 1, 36], color = 'red', label = 'Scatter 2')

plt.title('First chart!')
plt.ylabel('Y-Axis')
plt.xlabel('X-Axis')
plt.grid(True, color = 'k')
plt.legend(loc = 4) # plt.legend() would also work, but it will assign legends position as per default.

plt.show() # Always end with this, otherwise you will not be able to see anything!
