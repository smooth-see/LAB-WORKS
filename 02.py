import os 

path = '/Users/ermek/Documents/python/lab6_files'

print('Existence:', os.access(path, os.F_OK))
print('Readability:', os.access(path, os.R_OK))
print('Writability:', os.access(path, os.W_OK))
print('Executability:', os.access(path, os.X_OK))