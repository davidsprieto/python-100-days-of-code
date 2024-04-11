# Day 19/100 - Instances, State, and Higher Order Functions

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


screen.onkey(key="w", fun=move_forwards)


def move_backwards():
    turtle.back(10)


screen.onkey(key="s", fun=move_backwards)


def move_counter_clockwise():
    turtle.left(10)


screen.onkey(key="a", fun=move_counter_clockwise)


def move_clockwise():
    turtle.right(10)


screen.onkey(key="d", fun=move_clockwise)


def clear_drawing():
    turtle.penup()
    turtle.clear()
    turtle.home()
    turtle.pendown()


screen.onkey(key="c", fun=clear_drawing)


screen.listen()
screen.exitonclick()