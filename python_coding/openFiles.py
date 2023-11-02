import os

folder = "/home/apptunix/Pictures"
os.chdir(folder)
files = os.listdir()

file_path = 'path/to/your/file.txt'

try:
    with open("/home/apptunix/Pictures/kane.pdf", 'rb') as file:
        file_contents = file.read()
        print(f"File contents:\n{file_contents}")
except FileNotFoundError:
    print(f"The file at '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
