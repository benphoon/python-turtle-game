# Python Turtle Graphics Game - Space Turtle Chomp
import turtle

# Set Up Screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('navy')

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

    # boundary player checking x coordinate
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)

    # boundary player checking y coordinate
    if player.ycor() > 290 or player.ycor() < -290:
        player.right(180)
