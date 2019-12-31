import os
import pandas as pd

y = []

for x in os.listdir('C:\\Users\\Nirbhey Singh Pahwa\\PycharmProjects\\The project(BSE)\\Data_and_knowledge_2011_to_2013\\Knowledge'):# Make a program to check name of all files present in a directory.
    if x.endswith('.csv'): # This is just to have only scv files in x, you can change it to anything.
        y.append(x)

df = pd.DataFrame(y)

df.to_csv('example_for_names_present_in_dir.csv')

""" If you just want to check if a file is present

import os
import pandas as pd

path = 'C:\\Users\\Nirbhey Singh Pahwa\\PycharmProjects\\The project(BSE)\\Data_and_knowledge_2011_to_2013\\Knowledge\\'

y = []

str = '500035_BALAJI DIST.'
if (os.path.exists(path+str+'.csv')):
    y.append(str)

df = pd.DataFrame(y)

df.to_csv('C:\\Users\\Nirbhey Singh Pahwa\\PycharmProjects\\The project(BSE)\\example_for_names_present_in_dir.csv')

"""