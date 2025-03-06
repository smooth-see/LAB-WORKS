with open('ex5.txt', 'r') as file1:
    with open('ex7.txt', 'w') as file2:
        file2.write(file1.read())
        print(f"Successfully copied from {file1.name} to {file2.name}")