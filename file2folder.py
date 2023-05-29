# This code is trying to generate a folder based on file name and move the file to the corresponding folder
import glob
import os

def get_dir_name(filename):
    pos1 = filename.rfind('_')
    pos2 = filename.rfind('.')
    return filename[pos1+1:pos2]


for f in glob.glob('*.csv'):
    cwd = os.getcwd()
    dir_name = cwd + '/' + get_dir_name(f)
    print(dir_name)
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    os.rename(f, dir_name+ '/' + f)
