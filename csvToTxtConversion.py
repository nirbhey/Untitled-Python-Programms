textToBeRead1 = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Final year project\\Data\\eq020107_csv\\EQ020107.csv', 'r').read()
textToBeRead2 = open('C:\\Users\\Nirbhey Singh Pahwa\\Documents\\College(Engg.)\\Final year project\\Data\\eq020107_csv\\EQ020107.csv', 'r').readlines()

print(textToBeRead1)
print(textToBeRead2)

writeToNewFile = open('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example2.txt', 'w')

writeToNewFile.write(textToBeRead1)

writeToNewFile.close()
"""
# Cannot do this as "TypeError: write() argument must be str, not list"

writeToNewFile = open('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example2.txt', 'a')

writeToNewFile.write(textToBeRead2)

writeToNewFile.close()

"""
