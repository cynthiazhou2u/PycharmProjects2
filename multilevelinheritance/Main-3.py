from Vehicles import PassengerVehicle, CargoVehicle, Car, SemiTrailerTruck, Train

car_1 = Car("BMW", "M3", 2018, "Grey")
semi_truck_1 = SemiTrailerTruck(30000, "Diesel", 126560, "2 Months")
train_1 = Train(80,"Industrial", 250, 200)

print(f"The passenger vehicle is a {car_1.color} {car_1.year} {car_1.make} {car_1.model}.")
print("\n")

# In addition to the car_1 object using its own class methods, notice that it can use the methods from the
# PassengerVehicle class which it inherits from.
# This is single inheritance.

car_1.drive()       # Car class internal method
car_1.stop()        # Car class internal method
car_1.pick_up()     # PassengerVehicle class internal method
car_1.drop_off()    # PassengerVehicle class internal method
print("\n")

print(f"The cargo vehicle at is a semi-truck that takes {semi_truck_1.fuel}, \n"
      f"has {semi_truck_1.miles} miles and requires"
      f" a service every {semi_truck_1.service_cycle}.\n"
      f"This semi-truck has a maxload of: {semi_truck_1.maxload}LBS.")

# In addition to the semi_truck_1 object using its own class methods, notice that it can use the methods from the
# CargoVehicle class which it inherits from.
# This is single inheritance.

print("\n")
semi_truck_1.horn()             # SemiTrailerTruck class internal method
semi_truck_1.attach_trailer()   # SemiTrailerTruck class internal method
semi_truck_1.dettach_trailer()  # SemiTrailerTruck class internal method
semi_truck_1.weighing_in()      # SemiTrailerTruck class internal method
semi_truck_1.loading_cargo()    # CargoVehicle class internal method
semi_truck_1.unloading_cargo()  # CargoVehicle class internal method
print("\n")

print(f"This train is both a cargo and passenger vehicle that hauls {train_1.cargo_type} material and \n can carry"
      f" {train_1.number_of_passengers} passengers split between its {train_1.number_of_cars} cars. \n"
      f"The train has a max"
      f" speed of {train_1.top_speed}kms per hour.")

# In addition to the train_1 object using its own class methods, notice that it can use the methods from the
# CargoVehicle and the PassengerVehicle class as it inherits from both classes.
# This is an example of multiple inheritance.

print("\n")
train_1.attach_cars()       # Train class internal method
train_1.detach_cars()       # Train class internal method
train_1.loading_cargo()     # CargoVehicle class internal method
train_1.unloading_cargo()   # CargoVehicle class internal method
train_1.pick_up()           # PassengerVehicle class internal method
train_1.drop_off()          # PassengerVehicle class internal method

