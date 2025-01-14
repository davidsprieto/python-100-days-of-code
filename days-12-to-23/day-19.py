# Day 19/100 - Instances, State, and Higher Order Functions

from turtle import Turtle, Screen

# Etch-A-Sketch:
# turtle = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     turtle.forward(10)
#
#
# screen.onkey(key="w", fun=move_forwards)
#
#
# def move_backwards():
#     turtle.back(10)
#
#
# screen.onkey(key="s", fun=move_backwards)
#
#
# def move_counter_clockwise():
#     turtle.left(10)
#
#
# screen.onkey(key="a", fun=move_counter_clockwise)
#
#
# def move_clockwise():
#     turtle.right(10)
#
#
# screen.onkey(key="d", fun=move_clockwise)
#
#
# def clear_drawing():
#     turtle.penup()
#     turtle.clear()
#     turtle.home()
#     turtle.pendown()
#
#
# screen.onkey(key="c", fun=clear_drawing)
#
#
# screen.listen()
# screen.exitonclick()


# Turtle Racing Game:
import random
screen = Screen()
screen.setup(width=500, height=400)

can_race_start = False
user_input_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? (red, green, yellow, blue, orange, purple, or black)").capitalize()

# FIRST SOLUTION:
# red = Turtle(shape="turtle")
# red.color("red")
# red.penup()
# red.goto(x=-240, y=0)
#
# green = Turtle(shape="turtle")
# green.color("green")
# green.penup()
# green.goto(x=-240, y=-25)
#
# yellow = Turtle(shape="turtle")
# yellow.color("yellow")
# yellow.penup()
# yellow.goto(x=-240, y=25)
#
# blue = Turtle(shape="turtle")
# blue.color("blue")
# blue.penup()
# blue.goto(x=-240, y=-50)
#
# orange = Turtle(shape="turtle")
# orange.color("orange")
# orange.penup()
# orange.goto(x=-240, y=50)
#
# purple = Turtle(shape="turtle")
# purple.color("purple")
# purple.penup()
# purple.goto(x=-240, y=-75)
#
# black = Turtle(shape="turtle")
# black.color("black")
# black.penup()
# black.goto(x=-240, y=75)


# SECOND SOLUTION - OPTIMIZED CODE:
colors = ["red", "green", "yellow", "blue", "orange", "purple", "black"]
turtles = []

x = -240
y = 0
count = 0

for ti in range(0, len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[ti])
    t.penup()
    if count % 2 == 0:
        t.goto(x=x, y=y)
        y += 25
    else:
        t.goto(x=x, y=(y * -1))
    count += 1
    turtles.append(t)

if user_input_bet:
    can_race_start = True

winner = ""
while can_race_start:
    for t in turtles:
        rd = random.randint(0, 10)
        t.forward(rd)
        if t.xcor() >= 220:
            winner = t.pencolor().capitalize()
            can_race_start = False
            if winner == user_input_bet:
                print(f"Congratulations, {user_input_bet} won the race!")
            else:
                print(f"Sorry, {winner} won the race. You bet {user_input_bet} would win the race, better luck next time...")

screen.exitonclick()