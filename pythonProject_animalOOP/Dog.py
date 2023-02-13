# Importing the Animal Class from the Animal Module
from Animal import Animal


# Indicating that the Dog Class will inherit (attributes and methods)from the Animal Class
class Dog(Animal):

    def __init__(self, breed, gender, color, ears, mood):
        self.breed = breed          # Instance Variable
        self.gender = gender        # Instance Variable
        self.color = color          # Instance Variable
        self.ears = ears            # Instance Variable
        self.mood = mood            # Instance Variable

    def bark(self):
        print(f"This {self} is barking...")

    def wag_tail(self):
        print(f"This {self} is wagging its tail...")

    def pant(self):
        print(f"This {self} is panting..")
