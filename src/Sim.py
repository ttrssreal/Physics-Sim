import turtle
import random
import time
import numpy
import Vector
import Force

# create the main window

screen = turtle.Screen()
screen.bgcolor('black')
screen.title('physics')

grav_acc = -4

# global forces acting on all objects

globalForces = []
physicsObjects = []

# used for randomization

colors = ['green', 'orange', 'blue', 'red', 'purple']
shapes = ['circle', 'square', 'triangle']

# make two example forces for testing

gravity = Force.Force('Gravity', 0, grav_acc)
sideways = Force.Force('Sideways', 0.01, 0)

# add them to the global forces list to act on all objects

globalForces.append(gravity)
globalForces.append(sideways)


# a function to make a turtle or object

def createLife(shape='circle', color='red', width=1):
    obj = turtle.Turtle()
    obj.color('red')
    obj.shape(shape)
    obj.width(1)
    obj.yvel = 0
    obj.xvel = 0
    return obj


# user input to create specifyed num of random objects

for i in range(int(input('num:'))):
    physicsObjects.append(createLife(random.choice(shapes),
                          random.choice(colors), 1))

# main sim loop for physics

while True:

  # loops through all objects

    for object_num in physicsObjects:

    # for each object it loops through al global forces

        for force_num in globalForces:

        # add velocity to simulate acceleration

            object_num.xvel += force_num.x
            object_num.yvel += force_num.y

    # update positions

        object_num.sety(object_num.ycor() + object_num.yvel)
        object_num.setx(object_num.xcor() + object_num.xvel)

   # check for intersection with boundries

        if object_num.ycor() <= -200:
            object_num.yvel *= -1

        if object_num.ycor() < -199:
            object_num.sety(-200)

# upon application exit event

screen.mainloop()
