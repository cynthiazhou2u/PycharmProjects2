# class is a variable
# Below we are importing the Vehicle class from the Vehicle module."""
from vehicle import Vehicle

# In order to create an object from the Vehicle class, we define an object name
# and assign it the value of the Vehicle, passing in all the required arguments.
# In the background, Python is invoking the special __init__ method as seen in the Vehicle class.
car_1 = Vehicle("car", "Honda", "Civic", "2022", "black", 32000, False)
car_2 = Vehicle("truck", "Toyota", "Tundra", "2002", "silver", 14000, True)
car_3 = Vehicle("supercar", "McLaren", "GT", "2022", "black", 250000, False)

# The result is that three unique objects will be created from the Vehicle class.
# Printing out the instance variables for car_1
print("car_1 object instance variables:")
print(car_1.type)
print(car_1.manufacturer)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.price)
print(car_1.discount)
print("\n")

# Printing out the instance variables for car_2
print("car_2 object instance variables:")
print(car_2.type)
print(car_2.manufacturer)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print(car_2.price)
print(car_2.discount)
print("\n")

# Printing out the instance variables for car_3
print("car_3 object instance variables:")
print(car_3.type)
print(car_3.manufacturer)
print(car_3.model)
print(car_3.year)
print(car_3.color)
print(car_3.price)
print(car_3.discount)
print("\n")

# Accessing the object methods as defined within the Vehicle class.
car_1.drive()             #object_name.method
car_2.stall()
car_3.speeding()
print("\n")

# Notice that we can change Class Variables associated with the object as they are publicly accessible:
car_1.wheels = 2
car_1.is_drivable = False
# This will alter the defined Class Variables for that specific object:
print(car_1.wheels)
print(car_1.is_drivable)
print("\n")

# Altering the Class Variables for object car_3
car_3.has_engine = False
car_3.is_drivable = False
print(car_3.has_engine)
print(car_3.is_drivable)
print("\n")

# Notice that if we change the Class Variable from the Class level and not the level of the object
# that all objects created thereafter will have the new Class Variable attributes.
# Essentially by using the class to access the class variables we are changing the blueprint which
# will result in all objects created from the blueprint to inherit the same attributes
print("Number of Vehicle wheels defined as a Class Variable:")
print(Vehicle.wheels)
Vehicle.wheels = 1
Vehicle.is_drivable = False
print("\n")

print(f'old instances wheels:  {car_1.wheels}, {car_2.wheels},{car_3.wheels}')
print("\n")

# Creating a new car object.
# Notice that it has inherited the attribute changes that were made to the Class' Class Variables.
print("Creating a new car object after changing the Class Variable wheels to equal 1.")
car_4 = Vehicle("car", "Honda", "Civic", "2022", "black", 32000, False)
print(car_4.wheels)
print(car_4.is_drivable)


