# Multi-Level Inheritance: when a derived (child) class inherits another derived (child) class.
# Think Hierarchy: Organism (parent) > Mammal (Organism's child) > Ape (Mammal's child) > Guerrilla (Ape's child)

from Organism import Organism


class Mammal(Organism):

    def __init__(self, warm_blooded, number_of_legs, number_of_arms, land_animal, has_hair):
        self.warm_blooded = warm_blooded
        self.number_of_legs = number_of_legs
        self.number_of_arms = number_of_arms
        self.number_land_animal = land_animal
        self.has_fur = has_hair

    def runs(self):
            print("The mammal is running...")

    def eats(self):
            print("This mammal is eating...")

    def sleeps(self):
            print("This mammal is sleeping")

    def hides(self):
            print("This mammal is hiding...")