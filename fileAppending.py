textToAppend = '\nThis is appended text here!'

varToCallFile = open ('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example1.txt', 'a')

varToCallFile.write(textToAppend) # Even though we are appending and not writing(kind of like rewriting, where the file becomes complete blank and new data is written onto it

varToCallFile.close()
