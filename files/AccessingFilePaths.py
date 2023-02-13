import os

path = "C:\\Users\\drzho\\PycharmProjects\\files\\Sample.txt"
path_two = "C:/Users/drzho/PycharmProjects/files/"

# NOTE: Replace the paths with the directory paths of your own system!

# Remember the "\" is interpreted by Python as an escape sequence, but
# we need it to be interpreted as a regular backslash. Therefore,
# to ignore the escape sequence, the escape sequence itself needs to be
# escaped by another "\"


print("Checking Path 1:")
if os.path.exists(path):
    print("The file location exists.")
    print(f"This file path is: {path}")
    print("\n")
    if os.path.isfile(path):
        print("The location contains a real file.")
    elif os.path.isdir(path):
        print("This location contains a directory. ")
else:
    print("This file location doesn't exist.")

print("\n")
print("Checking Path 2:")
if os.path.exists(path_two):
    print("The file location exists.")
    print(f"This file path is: {path_two}")
    print("\n\f\f")
    if os.path.isfile(path_two):
        print("The location contains a real file.")
    elif os.path.isdir(path_two):
        print("This location contains a directory. ")
else:
    print("This file location doesn't exist.")