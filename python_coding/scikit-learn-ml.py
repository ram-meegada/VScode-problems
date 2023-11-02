import os

# Replace 'your_file.txt' with the actual file path you want to check
file_path = 'kane.jpg'

# Get the absolute path of the file
absolute_path = os.path.abspath(file_path)

if os.path.exists(absolute_path):
    print("Absolute Path:", absolute_path)
else:
    print("File does not exist or path is incorrect.")