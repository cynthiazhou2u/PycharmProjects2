# Duck Typing = the concept where the class of an object is less important than
# the methods and attributes which that class contains.
# Python will ignore the class type checking if the minimum methods and attributes are present.

# Python Interpreter: "If it looks like a duck, and it quacks like a duck, then it must be a duck."


class Duck:
    def waddle(self):
        print(f"This {self} duck is waddling...")

    def quack(self):
        print("This duck is quacking...")


class Goose:
    def waddle(self):
        print(f"This {self} duck is waddling...")

    def quack(self):
        print("This duck is quacking...")


class Chicken:
    def waddle(self):
        print(f"This {self} duck is waddling...")

    def quack(self):
        print("This duck is quacking...")


class Turkey:
    def waddle(self):
        print(f"This {self} duck is waddling...")

    def quack(self):
        print("This duck is quacking...")


class Farmer:

    # Notice that the "catch" method is expecting a "Duck" object. However, because Duck, Goose, Chicken
    # and Turkey all contain the same method signatures, the Python interpreter will assume that the object
    # passed in is in fact a Duck object regardless if it was actually a Goose, Chicken or Turkey object.
    # Method and attributes of a class take precedence over class names.

    # Python Interpreter: "If it looks like a duck, and it quacks like a duck, then it must be a duck."

    def catch(self, duck):
        duck.waddle()             #nested function calling
        duck.quack()
        print("Jim the farmer has caught the duck! Wait... Is it a duck?")


duck = Duck()
goose = Goose()              # => goose =Duck()
chicken = Chicken()
turkey = Turkey()


jim = Farmer()
print("Duck: \n")
jim.catch(duck)
print("\n")


# Gerald's catch method is given a Goose object, but because the Goose class has the same method signatures as
# the Duck class, and the catch method is expecting a Duck object, the interpreter will assume it is a Duck object.
gerald = Farmer()
print("Goose: \n")
gerald.catch(goose)
print("\n")

# Sam's catch method is given a Chicken object, but because the Chicken class has the same method signatures as
# the Duck class, and the catch method is expecting a Duck object, the interpreter will assume it is a Duck object.

sam = Farmer()
print("Chicken: \n")
sam.catch(chicken)
print("\n")

# Paul's catch method is given a Turkey object, but because the Turkey class has the same method signatures as
# the Duck class, and the catch method is expecting a Duck object, the interpreter will assume it is a Duck object.

paul = Farmer()
print("Turkey: \n")
paul.catch(turkey)
print("\n")

# Python Interpreter: "If it looks like a duck, and it quacks like a duck, then it must be a duck."
