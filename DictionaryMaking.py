testDictionary = {'data1': 'val1', 'data2': 'val2', 'data3': 'val3', 'data4': 'val4'}

print(testDictionary)

print(testDictionary['data2']) # To check a specific element of the dictionary.

testDictionary['data2'] = 'val0' # Reassigning values to data.

print(testDictionary)

testDictionary['data9'] = 'val9'

print(testDictionary)

del testDictionary['data2'] # To delete an element of the dictionary.

print(testDictionary)

testDictionary2 = {'data1': ['val1', 0], 'data2': ['val2', 1]}

print(testDictionary2['data1'])

print(testDictionary2['data2'][1])