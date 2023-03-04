"""
Task 2: This file is a module within the 'geom_classes' package that creates the 
'base' or 'parent' class for the other shape classes- square, circle, and triangle 
"""

import random

class Geom():
  geomType = 'Generic Geometry Type'
  
  # Constructor of the class: used to initialize an object
  def __init__(self):
    # Check out the names and the faker packages for random names
    self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
    self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
    self.type = "geometry"
  
  # This is a method that all children will inherit. 
  # In other words, all children will have this method without explicitly defining it. 
  def print_name(self):
    print('My name is',self.name, ', a', self.type, ', and my color is',self.color)

  # Another method: why we can call self.area without defining it here?
  def makeString(self):
    return f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Area: {self.area()}"
