textTobeRead1 = open ('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example1.txt', 'r').read() # This var will have all the text in this file as one variable

textTobeRead2 = open ('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example1.txt', 'r').readlines() # This var will have text stored in list, as separate items.

print(textTobeRead1,'\n')

print(textTobeRead2)

#Funny how you don't need a "extTobeRead2.close()" or "extTobeRead21.close()" here.