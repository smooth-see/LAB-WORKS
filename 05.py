def wlist_to_file(filename, data_list):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List written successfully to {filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

my_list = ["Say", "My", "Name.", "Heisenberg."]

file_name = "ex5.txt"

wlist_to_file(file_name, my_list)