# Python Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random
import os

# Set Up Screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('navy')
wn.bgpic('space-bg.gif')
wn.tracer(5)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()


# Set speed variable
speed = 1

# Create food
maxFoods = 10
foods = []
for count in range(maxFoods):
    food = turtle.Turtle()
    food.color("lightgreen")
    food.shape("circle")
    food.penup()
    food.speed(0)
    food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(food)
for food in foods:
    food.shapesize(.5)

# Define functions


def turn_left():
    player.left(30)


def turn_right():
    player.right(30)


def increase_speed():
    global speed
    speed += 1


def reduce_speed():
    global speed
    speed -= 1


def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) +
                  math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(reduce_speed, "Down")
while True:
    player.forward(speed)

    # boundary player checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        os.system('afplay bounce.mp3&')

    # boundary player checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
        os.system('afplay bounce.mp3&')

    # move food around
    for food in foods:
        food.forward(3)

        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            os.system('afplay bounce.mp3&')

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180)
            os.system('afplay bounce.mp3&')

        # collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290),
                             random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system('afplay chomp.mp3&')
