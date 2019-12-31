x = [0, 0, 0, 0, 0, 0, 0, 0, 0]

x.append(10)
x.insert(2, 99)
x[0] = 10

print(x)

x.remove(99) # Removes the first occurrence of the given data, here 99.
print(x)

x.remove(x[3]) # Remove the data from exact reference place.
print(x)

x.insert(2, 99)
print(x[2])

print(x[2 : 7]) # Slicing, to access only a part of list.

print(x[-1]) # To reference the last element

print(x[-2]) # To reference the second last element

print(x)

print(x.index(99)) # To find the index value of an item.

print(x.count(0)) # To count how many of this particular data is present in the list.
print("xa: ", x)
x.sort() # To sort a list.
print("xb: ", x)
y = x.index(0)

print(x)
print(y)