# Multi-Level Inheritance: when a derived (child) class inherits another derived (child) class.
# Think Hierarchy: Organism (parent) > Mammal (Organism's child) > Ape (Mammal's child) > Guerrilla (Ape's child)

from Ape import Ape


class Guerrilla(Ape):

    def __init__(self, hair_color, height, weight, gender, is_alpha, has_offspring, mood, name):

        self.hair_color = hair_color
        self.height = height
        self.weight = weight
        self.gender = gender
        self.is_alpha = is_alpha
        self.has_offspring = has_offspring
        self.mood = mood
        self.name = name

    def fighting(self):

        print(f"The guerrilla named {self.name} is fighting...")

    def foraging(self):
        print(f"The guerrilla named {self.name} is foraging...")

    def raging(self):
        print(f"The guerrilla named {self.name} is raging...")