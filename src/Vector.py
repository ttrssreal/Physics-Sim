class Vector:

    def __init__(
        self,
        x=1,
        y=1,
        name=None,
        ):
        self.x = x
        self.y = y
        self.name = name
        self.turtle = turtle.Turtle()

   # draws line...

    def drawLine(
        self,
        a,
        b,
        color='blue',
        width=5,
        ):
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

    # adds offset

        xpoint = x + self.x
        ypoint = y + self.y

    # draws vector

        self.drawLine([x, y], [xpoint, ypoint], 'blue')

  # set vector...

    def setVector(self, vec):
        self.x = vec[0]
        self.y = vec[1]

   # stuff

    def dotProduct(self, a, b):
        output = [0, 0]
        if len(a) == 2 and len(b) == 2:
            output[0] = a[0] * b[0]
            output[1] = a[1] * b[1]

        return output

  # gets vector...

    def getVector(self):
        return [self.x, self.y]

  # nothing

    def getAngleFromY(self):
        pass

  # sets magnitude

    def setMagnitude(self, mag):
        self.x *= mag / self.getMagnitude()
        self.y *= mag / self.getMagnitude()

  # gets magnitude

    def getMagnitude(self):
        return numpy.sqrt(self.x ** 2 + self.y ** 2)

  # clears drawings

    def clear(self):
        self.turtle.clear()
