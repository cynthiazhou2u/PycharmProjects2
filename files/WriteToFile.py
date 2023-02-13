
data1 = "This is the content that will be written to the file WriteToFile.txt" \
        " upon creation.\nNotice the 'w' parameter within the open() function. This" \
        " this will write to a file and additionally overwrite existing data.."

data2 = "Notice the 'a' parameter within the open() signifies that this text" \
        " will be appended to the file and not overwrite the existing data." \
        " running this multiple times will add this text block again to the " \
        " WriteToFile2.txt.\n"

# Try running this multiple times and notice that it will merely overwrite itself.
with open("WriteToFile.txt", "w") as file:
    file.write(data1)

print(open("WriteToFile.txt").read(),'\n\f\f')
# Try running this multiple times and notice that it will continue to append the text
# to the end of the file.
with open("WriteToFile2.txt", "a") as file2:
    file2.write(data2)
#   file2.read()           #io.UnsupportedOperation: not readable
print(open("WriteToFile2.txt").read())