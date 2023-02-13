# shutil useful methods:
# copyfile = copies the contents of a file
# copy() =  copyfile() + permission mode + destination can be a directory
# copy2() = copy + copies metadata (file timestamp data)

import shutil

shutil.copyfile("FileToCopy.txt", "CopiedFile.txt")     # source, destination (paths)

print(open("CopiedFile.txt").read())
# If you have an error, try using the full path to the file.

