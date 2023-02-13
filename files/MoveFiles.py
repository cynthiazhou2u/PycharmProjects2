import os, shutil

source = "FileToMove.txt"
destination = "C:/users/drzho/PycharmProjects/FileToMove.txt"
# Use the directory path for your own system's Desktop

# Remember the "\" is interpreted by Python as an escape sequence, but
# we need it to be interpreted as a regular backslash. Therefore,
# to ignore the escape sequence, the escape sequence itself needs to be
# escaped by another "\"


try:
    if os.path.exists(destination):
        print("The file already exists in the current directory.")
    else:
        os.replace(source, destination)
        print(f"{source} was moved to this destination: {destination}")
except FileNotFoundError:
    print(f"{source} file not found...")

shutil.move("C:/users/drzho/PycharmProjects/FileToMove.txt","FileToMove.txt")