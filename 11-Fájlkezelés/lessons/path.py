import os
# https://note.nkmk.me/en/python-script-file-path/#osgetcwd-and-__file__

# Error if not exists
# os.rename('filename.txt', 'newfilename.txt')

# Listing all files and directories
print(os.listdir())

# source = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/source/filename.txt'
# destination = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/destination'
# # Move the content of 
# # source to destination 
# dest = shutil.move(source, destination) 
# dest = shutil.copy(source, destination) 
# remove dir NOT THROW ERROR IF NOT EXISTS
print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('abspath:     ', os.path.abspath(__file__))
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), 'text.txt'))

