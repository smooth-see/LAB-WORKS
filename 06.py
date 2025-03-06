import string
import os

path = r'/Users/ermek/Documents/python/lab6_files'
os.makedirs(path)

def create_text_files():
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt"
        open(f"{path}/{filename}", 'w')
        print(f"Created: {filename}")

create_text_files()