# Multi-Level Inheritance: when a derived (child) class inherits another derived (child) class.
# Think Hierarchy: Organism (parent) > Mammal (Organism's child) > Ape (Mammal's child) > Guerrilla (Ape's child)


class Organism:

    alive = True
    light_sensitivity = True
    eukaryotic = True

    def reproduce(self):
        print("This organism has reproduced...")

    def energy_process(self):
        print("This organism has processed energy...")

    def growth(self):
        print("This organism is growing...")

