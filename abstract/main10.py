# Abstract classes are classes that contain one or more abstract methods.
# An Abstract methods is a method that is declared, but contained no implementation.
# Abstract classes cannot be instantiated (create objects), and require subclasses to provide
# implementations of the abstract methods.

from abc import ABC, abstractmethod    #abc - abstract based class


class Vehicle(ABC):

    # This annotation below declares this class as an abstract class. This will prevent the
    # Vehicle class from being instantiated.
    # Additionally, the @abstractmethod annotation will force any child classes of Vehicle
    # to create its own implementation of any abstract methods within the abstract class (drive).
    # This is an example of method overriding.

    @abstractmethod
    def drive(self):
        pass    # The pass keyword indicated that is method is undefined (no implementation).

    @abstractmethod
    def stop(self):
        pass    # The pass keyword indicated that is method is undefined (no implementation)


class Truck(Vehicle):

    def drive(self):
        print("The truck is driving along the dirt road...")

    def stop(self):
        print("the truck stops...")


class Sedan(Vehicle):

    def drive(self):
        print("The sedan is driving on the highway...")

    def stop(self):
        print("the sedan stops...")

# Notice that if we uncomment the Motorcycle class below, that the Python interpreter will yield
# an error, as Motorcycle inherits from the Vehicle class (abstract class) and therefore must provide
# an implementation for the inherited abstract method (drive).


class Motorcycle(Vehicle):
    def drive(self):
        print(f'{self} is riding..')

    def stop(self):
        print(f'{self} stops..:)')

truck_1 = Truck()
sedan_1 = Sedan()

truck_1.drive()
sedan_1.drive()
truck_1.stop()
sedan_1.stop()

bike_1 = Motorcycle()
bike_1.drive()
bike_1.stop()
