# Day 18/100 - Turtle & The GUI

import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("olive")
t.colormode(255)

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

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]


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
# turtle.pensize(10)
# turtle.speed("fastest")
# directions = [0, 90, 180, 270]
#
# for _ in range(100):
#     turtle.color(random.choice(colors))
#     turtle.forward(20)
#     turtle.setheading(random.choice(directions))


# Generate random RGB Colors
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rc = (r, g, b)
#     return rc


#
#
# for _ in range(100):
#     turtle.color(random_color())
#     turtle.forward(20)
#     turtle.setheading(random.choice(directions))


# Draw a spirograph
# turtle.speed("fastest")
#
#
# def draw_spirograph(gap):
#     for _ in range(int(360 / gap)):
#         turtle.color(random_color())
#         turtle.circle(100)
#         turtle.setheading(turtle.heading() + gap)
#
#
# draw_spirograph(50)

# screen = Screen()
# screen.exitonclick()


# Day 18 Project - Spot (Hirst) Painting:
colors = colorgram.extract("/Users/david/PycharmProjects/python-100-days-of-code/days-12-to-23/day-18-turtle-gui/image.jpeg", 34)
length_of_colors = len(colors)
tuple_list_of_colors = []

for i in range(length_of_colors):
    color_tuple = (colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b)
    tuple_list_of_colors.append(color_tuple)

turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()
turtle.setheading(220)
turtle.forward(300)
turtle.setheading(0)

count = 100
turns = 1

for count in range(1, count + 1):
    turtle.dot(20, random.choice(tuple_list_of_colors))
    turtle.forward(50)
    if count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        if turns % 2 == 0:
            turtle.setheading(360)
        else:
            turtle.setheading(180)
        turns += 1
        turtle.forward(50)


screen = Screen()
screen.exitonclick()