#  Creating a directory
import os
import shutil 

os.mkdir('directory')

# Renaming a dir ERROR IF NOT EXISTS
os.rename('directory', 'newdirectory')

# Changing the current working directory
os.chdir('directory')

# Getting the current working directory
print(os.getcwd())

# Removing a directory, ERROR IF NOT EXISTS
os.rmdir('directory')

# Listing all files and directories
print(os.listdir())

source = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/source'
destination = 'C:/Users/Rajnish/Desktop/GeeksforGeeks/destination'
# Move the content of 
# source to destination 
dest = shutil.move(source, destination) 
dest = shutil.copy(source, destination) 
# remove dir NOT THROW ERROR IF NOT EXISTS
shutil.rmtree()