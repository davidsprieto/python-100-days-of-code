# Day 1/100: Working with Variables & print(), input(), len()

# print function - printing to the console
print("Hello World!")

# string manipulation
print("Day 1 - Python Print Function\n"
      "The function is declared like this:\n"
      "print('what to print')")

# string concatenation
print("Hello " + "world")

# input function - taking input
print("Hello " + input("What is your name? "))

# print the length of name
print(len(input("What is your name? ")))

# python variables
name = "David"
print(name)

# refactor above 'print the length of name' code using separate variables
name = input("What is your name? ")
length = len(name)
print(length)

# Day 1 Project - Band Name Generator
print("Welcome to the Band Name Generator.")
user_city_name = input("What's the name of the city you grew up in?\n")
user_pet_name = input("What's your pet's name?\n")
print("Your band name could be " + user_city_name + " " + user_pet_name + "\n\n")
