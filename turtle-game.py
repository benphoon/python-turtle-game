# Python Turtle Graphics Game - Space Turtle Chomp
import turtle

# Set Up Screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('navy')

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()

# Set speed variable
speed = 1

# Define movement functions

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


# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, "Left")
turtle.onkey(turn_right, "Right")
turtle.onkey(increase_speed, "Up")
turtle.onkey(reduce_speed, "Down")
while True:
    player.forward(speed)
