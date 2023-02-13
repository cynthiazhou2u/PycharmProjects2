class School:

    max_capacity = None
    number_of_classrooms = None
    number_of_floors = None


def build_school(school, max_capacity, number_of_classrooms, number_of_floors):

    # This is a standalone function. Notice the lack of an indent. An indented "def" would
    # make this a method of the School class.

    # This function takes a School object and three additional arguments.
    # We will set the class variables of the School object via the arguments passed into the "build_school" function.

    school.max_capacity = max_capacity
    school.number_of_classrooms = number_of_classrooms
    school.number_of_floors = number_of_floors


# Initializing three objects.
school_1 = School()
school_2 = School()
school_3 = School()

# We will call the build_school function and supply each with a School object and the other three arguments.
# This will set the class variables for each created object (School).
build_school(school_1, 1800, 20, 4)
print(f"This school has a maximum capacity of {school_1.max_capacity} with {school_1.number_of_classrooms} classrooms and"
      f" {school_1.number_of_floors} floors on campus.")
print("\n")


build_school(school_2, 2400, 30, 6)
print(f"This school has a maximum capacity of {school_2.max_capacity} with {school_2.number_of_classrooms} classrooms and"
      f" {school_2.number_of_floors} floors on campus.")
print("\n")

build_school(school_3, 3600, 40, 8)
print(f"This school has a maximum capacity of {school_3.max_capacity} with {school_3.number_of_classrooms} classrooms and"
      f" {school_3.number_of_floors} floors on campus.")
print("\n")