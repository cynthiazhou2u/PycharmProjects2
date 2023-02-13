from Animal import Animal
from Bird import Bird
from Dog import Dog

# Creating an Animal Object
animal_1 = Animal()

# Creating a Bird Object that will inherit class variables and class methods from the Parent Class.
bird_1 = Bird(True, False, "Owl", "Male", "Blue", "Happy")

# Creating a Dog Object that will inherit class variables and class methods from the Parent Class.
dog_1 = Dog("Boxer", "Female", "Brown", "Floppy", "Cranky")

# Accessing the Animal Class Variable using all three objects.
# Notice that the child class objects (bird and dog) can access the animal Class Variable.
print("Accessing the Animal Class Variable using all three objects:")
print(animal_1.alive)
print(bird_1.alive)
print(dog_1.alive)
print("\n")

# Animal object using its methods
print("Animal object using its methods:")
animal_1.play()
animal_1.eat()
animal_1.sleep()
print("\n")

# Bird object accessing its parent (Animal) methods
print("Bird object accessing its parent (Animal) methods:")
bird_1.play()
bird_1.eat()
bird_1.sleep()
print("\n")

# Bird object accessing its parent (Animal) methods
print("Bird object accessing its parent (Animal) methods:")
dog_1.play()
dog_1.eat()
dog_1.sleep()
print("\n")

# Bird object accessing its specific object methods.
print("Bird object accessing its specific object methods:")
bird_1.fly()
bird_1.peck()
bird_1.tweet()
print("\n")

# Dog object accessing its specific object methods.
print("\n")
dog_1.bark()
dog_1.wag_tail()
dog_1.pant()
print("\n")
