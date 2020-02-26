import os.path

# Path were the files will be stored
save_path = 'D:\Learn Python\projects'
# Request the user to enter a filename
file_name = input('Enter file name: ')
# combines the path and the filename
stored_file = os.path.join(save_path, file_name + '.txt')

# Creates a new file and stores it
new_file = open(stored_file, 'a')
# ask the user to add data to the file
data = input('Add text to your file.\n')
new_file.write(f'\n{data}')
new_file.close()
