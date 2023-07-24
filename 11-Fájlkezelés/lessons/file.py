import os
import shutil


# Copy Single File
# In this example, we are copying the profit.txt file from the report folder to the account folder.


src_path = r"E:\demos\files\report\profit.txt"
dst_path = r"E:\demos\files\account\profit.txt"
shutil.copy(src_path, dst_path)
print('Copied')

# Copy All Files From A Directory
source_folder = r"E:\demos\files\reports\\"
destination_folder = r"E:\demos\files\account\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)



# COPY
src_folder = r"E:\demos\files\reports"
dst_folder = r"E:\demos\files\account"
src_file = src_folder + "\profit.txt"
dst_file = dst_folder + "\profit.txt"
shutil.copyfile(src_file, dst_file)
print('Copied')

os.unlink(os.path.join(os.path.dirname(__file__), 'text.txt'))