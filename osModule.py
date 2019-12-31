import os
import time

curDir = os.getcwd() # cwd = current working directory.
print(curDir)

os.mkdir('newDir')

time.sleep(2)

os.rename('newDir', 'newDir2')
time.sleep(2)

os.rmdir('newDir2')

# os.rmdir('csvExampleFile.csv') This will not work.