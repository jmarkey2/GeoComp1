from geom_classes import geom
import math as mth

class Circle(geom.Geom):
  
  def __init__ (self, radius):
    self.radius = radius
    super().__init__()
    self.type = 'circle'

  # area method  
  def area(self):
     return mth.pi * self.radius **2