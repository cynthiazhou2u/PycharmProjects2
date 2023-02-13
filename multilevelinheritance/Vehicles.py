# In this example on Multiple Inheritance, all classes will be represented in this one module(file).
# This allows for rapid prototyping and testing of functionality, although,
# separating your classes into their own self-contained modules (files) is considered best practice.

# In this example, we will have two top-level classes (parents): PassengerVehicle and CargoVehicle.
# Additionally, we will have three child classes: Car, SemiTrailerTruck, Train.
# With Multiple Inheritance, a class can inherit attributes and behavior from multiple parent classes.

class PassengerVehicle:

    def pick_up(self):
        print("Picking up potential passengers...")

    def drop_off(self):
        print("Dropping off potential passengers...")


class CargoVehicle:

    def loading_cargo(self):
        print("Loading up the cargo...")

    def unloading_cargo(self):
        print("Unloading up the cargo...")


class Car(PassengerVehicle):

    # This is an example of single inheritance.

   def __init__(self, make, model, year, color):
       self.make = make
       self.model = model
       self.year = year
       self.color = color

   def drive(self):
       print("The car is driving...")

   def stop(self):
       print("The car is stopping...")


class SemiTrailerTruck(CargoVehicle):

    # This is an example of single inheritance.

    def __init__(self, maxload, fuel, miles, service_cycle):
        self.maxload = maxload
        self.fuel = fuel
        self.miles = miles
        self.service_cycle = service_cycle

    def horn(self):
        print("The semi-truck honks its horn...")

    def weighing_in(self):
        print("Weighing in at the weigh station...")

    def attach_trailer(self):
        print("attaching trailer...")

    def dettach_trailer(self):
        print("detaching trailer...")


class Train(PassengerVehicle, CargoVehicle):

    # The Train class in demonstrating multiple inheritance by inheriting from both the
    # PassengerVehicle and CargoVehicle classes

    def __init__(self, number_of_cars, cargo_type, number_of_passengers, top_speed):
        self.number_of_cars = number_of_cars
        self.cargo_type = cargo_type
        self.number_of_passengers = number_of_passengers
        self.top_speed = top_speed

    def attach_cars(self):
        print(f"Attaching cars to train at {self}...")

    def detach_cars(self):
        print("detaching cars to train...")
