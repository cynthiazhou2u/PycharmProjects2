# Multi-Level Inheritance: when a derived (child) class inherits another derived (child) class.
# Think Hierarchy: Organism (parent) > Mammal (Organism's child) > Ape (Mammal's child) > Guerrilla (Ape's child)

from Mammal import Mammal


class Ape(Mammal):

    def __init__(self, climbs, grooms, has_finger_nails, has_opposable_thumbs, has_prehensility):

        self.climbs = climbs
        self.grooms = grooms
        self.has_finger_nails = has_finger_nails
        self.has_opposable_thumbs = has_opposable_thumbs
        self.has_prehensility = has_prehensility


    def climbing(self):
         print("This ape is climbing...")

    def grooming(self):
        print("This ape is grooming...")

    def communicating(self):
        print("this ape is communicating...")