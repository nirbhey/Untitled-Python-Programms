from glob import glob
import sys
import os

if len(sys.argv) == 2:
    base_dir = (sys.argv[1])
    if os.path.exists(base_dir):
        list_of_xl_files = glob(os.path.join(base_dir,"**//*.xlsx")) + glob(os.path.join(base_dir,"**//*.xls"))
        with open("xl_list.txt", 'w') as f:
            for file in list_of_xl_files:
                f.write(file)
                f.write("\n")
    else:
        print("Path does not exist!")
else:
    print('Usage %s "base directory"', sys.argv[0])