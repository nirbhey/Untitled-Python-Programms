
import pandas as pd

df = pd.DataFrame({'Shit': [1, 3, 4, 5, 5], 'Shit2': [1, 3, 4, 5, 5], 'Shit3':[1, 3, 4, 5, 5]})
df.set_index('Shit', inplace=True)
df.to_csv('shit.csv')

df = pd.read_csv('shit.csv')
df.columns = ['a', 'b', 'c']
df.to_csv('shit.csv')

'''
The below code makes a new file which keeps the old data and adds new data at the top of old data and then saves it as the same name, giving an illusion of appending, where as it is just re-witting.
'''

csv = '.csv'
varToReadFile = open('shit'+csv, 'r').read() # This can be any variable to open / create file, it van be var also instead of varToOpenFile
print(varToReadFile)
varToWriteFile = open('shit.csv', 'w') # This can be any variable to open / create file, it van be var also instead of varToOpenFile
varToWriteFile.write("abc, abe, abd\n"+varToReadFile)
varToWriteFile.close()