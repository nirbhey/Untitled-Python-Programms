"""
Assumptions;
1. All values will be numerical.
2. There are 3 columns, Id, classes enrolled.
3. In the beginning the number of rows are equal to the cache size.
4. Cache size will be defined only before running the program.
"""
import pandas as pd
import time

least_recent_access = 0
df = pd.read_csv('file_name.csv')
max_size = [20]
list_ID_LRU = list(df['ID'])

def check_ID(ID_var):

    try:
        df.set_index("ID", inplace=True)
        idx = list_ID_LRU.index(ID_var)
        if idx == (len(list_ID_LRU) - 1):
            list_ID_LRU[:] = [list_ID_LRU[idx]] + list_ID_LRU[:idx]
        else:
            list_ID_LRU[:] = [list_ID_LRU[idx]] + list_ID_LRU[:idx] + list_ID_LRU[idx:]
        df.drop(int(ID_var), inplace=True)
        df.reset_index(inplace=True)
    except Exception as e:
        if len(list_ID_LRU) + 1 > max_size[0]:
            df.drop(list_ID_LRU[-1], inplace=True)
            list_ID_LRU[:] = [ID_var] + list_ID_LRU[:-1]
        else:
            list_ID_LRU[:] = [ID_var] + list_ID_LRU[:]
        df.reset_index(inplace=True)

def save_file():

    df.set_index('marks', inplace=True)
    df.sort_index(inplace=True)
    df.to_csv('file_name.csv')
    print("saving the cache in the file.")
    print("Note: This program will now close.")
    time.sleep(2)

# Create, Read, Update, Delete

def create():
    df.set_index('marks', inplace=True)
    df.sort_index(inplace=True)
    df.reset_index(inplace=True)

def read():

    try:
        print("Please enter the ID you want to access (or) enter 0 to view complete cache:")
        x = int(input())
        if x == 0:
            df.set_index("marks", inplace=True)
            df.sort_index(inplace=True)
            print(df)
            df.reset_index(inplace=True)
        else:
            df.set_index("ID", inplace=True)
            print(df.ix[x])
            idx = list_ID_LRU.index(x)
            if idx == (len(list_ID_LRU) - 1):
                list_ID_LRU[:] = [list_ID_LRU[idx]] + list_ID_LRU[:idx]
            else:
                list_ID_LRU[:] = [list_ID_LRU[idx]] + list_ID_LRU[:idx] + list_ID_LRU[idx + 1:]

            df.reset_index(inplace=True)
    except Exception as e:
        df.reset_index(inplace=True)
        print("Please enter a valid input!")
        read()

def update():

    print("Please enter the following details:\n")
    ID_var = int(input("Please enter student's ID:"))
    classes_enrolled_var = int(input("Please enter classes enrolled:"))
    marks_var = int(input("Please enter marks:"))
    check_ID(ID_var)
    return marks_var, ID_var, classes_enrolled_var

def delete():

    try:
        df.set_index("ID", inplace=True)
        print(df)
        print("Please Enter the ID you want to delete:")
        x = int(input())
        df.drop(x, inplace=True)
        print("ID [" + str(x) + "] has been deleted")
        df.reset_index(inplace=True)
        list_ID_LRU.remove(x)

    except Exception as e:
        print("Invalid input!")
        df.reset_index(inplace=True)
        delete()


print("Welcome to the cache of assignment 1!\n \n  You have just CREATED a cache!")
print("The cache size is: " + str(max_size[0]))
create()

while True:
    print()
    try:
        x = int(input("Please enter the corresponding integer for its operation:\n1 To READ\n2 To UPDATE\n3 To DELETE\n4 To EXIT\n"))
        print()
        if (x < 6) & (x > 0):

            if x == 1:
                read()

            elif x == 2:
                marks_var, ID_var, classes_enrolled_var = update()
                df = df.append({'marks': marks_var, 'ID': ID_var, 'classes_enrolled': classes_enrolled_var},
                               ignore_index=True)
                print("Update successful!\n")


            elif x == 3:
                delete()

            else:
                save_file()
                exit()

        else:
            x = 1/0

    except Exception as e:
        print("Please enter a valid input!")