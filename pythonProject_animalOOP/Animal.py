# This class will serve as the "Parent" Class which the Bird and Dog class will inherit from.
class Animal:

    alive = True    # Class Variable

    # Since this is a generic class, we will not include any instance variables.
    # Although you can do so if desired.
    # As such, we will not need to define the special function "__init__"
    # since we are not defining any instance variables.

    def eat(self):
        print("This animal is eating...")

    def sleep(self):
        print("This animal is sleeping...")

    def play(self):
        print("This animal is playing..")

