import Vector, turtle


#just an alias for "Vector" class
class Force(Vector.Vector):
  
  def __init__(self, name=None, x=0, y=0):
    self.x = x
    self.y = y
    self.name = name
    self.turtle = turtle.Turtle()
