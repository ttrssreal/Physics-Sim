import turtle, random, time, numpy, Vector, Force

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("physics")

grav_acc = -4

globalForces = []
physicsObjects = []

colors = ["green", "orange", "blue", "red", "purple"]
shapes = ["circle", "square", "triangle"]

gravity = Force.Force("Gravity", 0, grav_acc)
sideways = Force.Force("Sideways", 0.01, 0)

globalForces.append(gravity)
globalForces.append(sideways)

def createLife(shape="circle", color="red", width=1):
  obj = turtle.Turtle()
  obj.color("red")
  obj.shape(shape)
  obj.width(1)
  obj.yvel = 0
  obj.xvel = 0
  return obj

for i in range(int(input("num:"))):
  physicsObjects.append(createLife(random.choice(shapes), random.choice(colors), 1))

while True:

  for k in physicsObjects:
    for i in globalForces:
        k.xvel += i.x
        k.yvel += i.y
        
    k.sety(k.ycor()+k.yvel)
    k.setx(k.xcor()+k.xvel)

    if k.ycor() <= -200:
      k.yvel *= -1

    if k.ycor() < -199:
      k.sety(-200)

  
screen.mainloop()
