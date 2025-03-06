import os 

path = r'/Users/ermek/Documents/pyton/lab6_files/test.txt'
name = os.path.basename(path)

if os.path.exists(path):
    print(f'File "{name}" exists')
    if os.access(path, os.W_OK):
        print(f'File "{name}" can be deleted')
        os.remove(path)
        print(f'"{name}" is deleted')
    else:
        print(f'File "{name}" can\'t be deleted')
else:
    print(f'File "{name}" does\'t exist')