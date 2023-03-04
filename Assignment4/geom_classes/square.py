"""
Task 2: This file is a module within the 'geom_classes' package that creates the square class and provides a method for computing 
the area of an instance in which it is used. 
"""

from geom_classes import geom

class Square(geom.Geom):
  
  def __init__ (self,side):
    super().__init__()
    self.side = side
    self.type = "square"

  # area method  
  def area(self):
     return self.side **2