# Day 18/100 - Turtle & The GUI

from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("olive")

# Draw a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# Draw a dashed line
# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]


# Draw different shapes
# def draw_shape(s, d, e):
#     """A method that draws shapes based on input where s = starting sides (minimum 3), d = distance, and e = ending sides"""
#     while s <= e:
#         turtle.color(random.choice(colors))
#         for _ in range(s):
#             turtle.forward(d)
#             turtle.right(360 / s)
#         s += 1


# draw_shape(3, 100, 9)


# Draw a random walk
turtle.speed(8)
turtle.pensize(10)
directions = [0, 90, 180, 270]

for _ in range(100):
    turtle.color(random.choice(colors))
    turtle.forward(20)
    turtle.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
