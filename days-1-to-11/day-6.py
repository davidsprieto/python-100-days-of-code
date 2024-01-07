# Day 6/100: Python Functions, Karel, and While Loops

# Defining a function
def my_function(name):
    print(f"Hello, {name}")


my_function("David")


# While loops
count = 5
while count > 0:
    print(count)
    count -= 1

# Functions and While loops syntax was learned using: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# Day 6 Project - Escape the Maze:
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if not front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     elif not front_is_clear() and not right_is_clear():
#         turn_around()
#     elif right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()