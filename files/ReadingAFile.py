

# FileNotFoundError

try:
    with open("C:/Users/drzho/PycharmProjects/files/Sample.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found...")

print("\n\f\f a second try \f\f")

# Simulating a FileNotFoundError:
try:
    with open("C:FileThatDoesNotExist") as file2:
        print(file2.read())
except FileNotFoundError:
    print("That file was not found...")