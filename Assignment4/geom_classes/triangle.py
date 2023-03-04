#Task 1: add a class of Triangle

from geom_classes import geom

#create a Triangle class that is a subclass of Geom
class Triangle(geom.Geom):
#Initialize the attributes for a given instance of when the class is called
    def __init__ (self, base, height):
        self.base = base
        self.height = height
        super().__init__()
        self.type = 'triangle'
#create a method for finding the area for a given triangle object
    def area (self):
        return self.base *self.height * .5