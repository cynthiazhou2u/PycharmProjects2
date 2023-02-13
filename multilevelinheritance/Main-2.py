# Multi-Level Inheritance: when a derived (child) class inherits another derived (child) class.
# Think Hierarchy: Organism (parent) > Mammal (Organism's child) > Ape (Mammal's child) > Guerrilla (Ape's child)

from Guerrilla import Guerrilla


guerrilla_1 = Guerrilla("black", "6ft", "500lbs", "male", True, True, "happy", "Gerald")

# Accessing the class variable of the Organism class:
print("Organisms class variables being accessed by the guerilla_1 object:")
print(guerrilla_1.alive)
print(guerrilla_1.light_sensitivity)
print(guerrilla_1.eukaryotic)
print("\n")

# Accessing guerrilla_1's instance variables:
print("guerilla_1 object accessing its instance variables:")
print(guerrilla_1.hair_color)
print(guerrilla_1.height)
print(guerrilla_1.weight)
print(guerrilla_1.gender)
print(guerrilla_1.is_alpha)
print(guerrilla_1.has_offspring)
print(guerrilla_1.mood)
print(guerrilla_1.name)
print("\n")

# The guerrilla_1 object has access to its own internal methods
print("guerrilla_1 accessing its internal methods:")
guerrilla_1.fighting()
guerrilla_1.foraging()
guerrilla_1.raging()
print("\n")

# The guerrilla_1 object has access to the methods belonging to the Ape class (parent class):
print("guerilla_1 object accessing the methods belonging to the Ape class (parent class):")
guerrilla_1.climbing()
guerrilla_1.grooming()
guerrilla_1.communicating()
#print(guerrilla_1.climbs)    # can't access parent class's instance variable, private inside __init__
print("\n")

# The guerrilla_1 object has access to the methods belonging to the Mammal class (grandparent class):
print("guerrilla_1 object accessing the methods belonging to the Mammal class (grandparent class):")
guerrilla_1.runs()
guerrilla_1.eats()
guerrilla_1.sleeps()
guerrilla_1.hides()
print("\n")

# The guerrilla_1 object has access to the methods belonging to the Organism class (Great grandparent class):
print("guerrilla_1 accessing the methods belonging to the Organnism class (great grandparent class):")
guerrilla_1.reproduce()
guerrilla_1.energy_process()
guerrilla_1.growth()
print("\n")