import turtle, random, time, numpy, Vector, Force

#create the main window
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("physics")

grav_acc = -4

#global forces acting on all objects
globalForces = []
physicsObjects = []

#used for randomization
colors = ["green", "orange", "blue", "red", "purple"]
shapes = ["circle", "square", "triangle"]

#make two example forces for testing
gravity = Force.Force("Gravity", 0, grav_acc)
sideways = Force.Force("Sideways", 0.01, 0)

#add them to the global forces list to act on all objects
globalForces.append(gravity)
globalForces.append(sideways)

#a function to make a turtle or object
def createLife(shape="circle", color="red", width=1):
  obj = turtle.Turtle()
  obj.color("red")
  obj.shape(shape)
  obj.width(1)
  obj.yvel = 0
  obj.xvel = 0
  return obj

#user input to create specifyed num of random objects
for i in range(int(input("num:"))):
  physicsObjects.append(createLife(random.choice(shapes), random.choice(colors), 1))

#main sim loop for physics
while True:

  # loops through all objects
  for k in physicsObjects:
  
    #for each object it loops through al global forces
    for i in globalForces:
    
        #add velocity to simulate acceleration
        k.xvel += i.x
        k.yvel += i.y
    
    #update positions
    k.sety(k.ycor()+k.yvel)
    k.setx(k.xcor()+k.xvel)
    
    
   #check for intersection with boundries
    if k.ycor() <= -200:
      k.yvel *= -1

    if k.ycor() < -199:
      k.sety(-200)

#upon application exit event
screen.mainloop()
