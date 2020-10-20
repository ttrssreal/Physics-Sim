class Vector:
  
  def __init__(self, x=1, y=1, name=None):
    self.x = x
    self.y = y
    self.name = name
    self.turtle = turtle.Turtle()

  def drawLine(self, a, b, color="blue", width=5):
    self.turtle.color(color)
    self.turtle.shapesize(0.01)
    self.turtle.speed(0)
    self.turtle.width(width)
    self.turtle.penup()
    self.turtle.goto(a[0], a[1])
    self.turtle.pendown()
    self.turtle.goto(b[0], b[1])
    self.turtle.penup()

  def displayVector(self, x=0, y=0):
    xpoint = x + self.x
    ypoint = y + self.y
    self.drawLine([x, y], [xpoint, ypoint], "blue")

  def setVector(self, vec):
    self.x = vec[0]
    self.y = vec[1]

  def dotProduct(self, a, b):
    output = [0, 0]
    if len(a) == 2 and len(b) == 2:
      output[0] = a[0] * b[0]
      output[1] = a[1] * b[1]

    return output

  def getVector(self):
    return [self.x, self.y]

  def getAngleFromY(self):
    pass

  def setMagnitude(self, mag):
    self.x *= mag/self.getMagnitude()
    self.y *= mag/self.getMagnitude()

  def getMagnitude(self):
    return numpy.sqrt((self.x**2)+(self.y**2))

  def clear(self):
    self.turtle.clear()
