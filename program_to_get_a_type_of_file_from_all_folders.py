from glob import glob
from tqdm import tqdm
import os

list_of_dirs = []
[list_of_dirs.append(x[0]) for x in os.walk("./")]
for i in tqdm(range(len(list_of_dirs)), 'Directory: '):
	list_of_xl_files = glob(os.path.join(list_of_dirs[i],'*.xlsx')) + glob(os.path.join(list_of_dirs[i],'*.py'))
	with open("xl_list.txt", 'a') as f:
		for file in list_of_xl_files:
			f.write(file)
			f.write("\n")