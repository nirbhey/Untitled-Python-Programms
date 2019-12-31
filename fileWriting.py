writingText = 'This is the test text.\nNew line!'

varToOpenFile = open('C:\\Users\\Nirbhey Singh Pahwa\\Desktop\\example1.txt', 'w') # This can be any variable to open / create file, it van be var also instead of varToOpenFile

varToOpenFile.write(writingText)

varToOpenFile.close()