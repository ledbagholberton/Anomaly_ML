import os 
import glob 

def delete_files(path="static/images/"):
    files = glob.glob(path + '*')
    for f in files: 
        os.remove(f) 