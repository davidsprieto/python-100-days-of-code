# Day 5/100: Python Loops

import random

fruits = ["apple", "peach", "pear"]

for fruit in fruits:
    print(fruit)

# Average Height Challenge
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_of_heights = 0
amount_of_students = 0
for height in student_heights:
    sum_of_heights += height
    amount_of_students += 1
average_height = round(sum_of_heights / amount_of_students)
print(f"The average height of the students is: {average_height}")


# High Score Challenge
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
high_score = student_scores[0]
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"The highest score in the class is: {high_score}")


# Adding Even Numbers Challenge - For loop with range()
sum_of_evens = 0
for n in range(2, 101, 2):
    sum_of_evens += n
print(sum_of_evens)


# FizzBuzz Challenge
for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 3 == 0:
        print("Fizz")
    else:
        print(n)


# Day 5 Project - Create a Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))
nr_symbols = int(input(f"How many symbols would you like?: "))

# Easy Level - Order not randomized:
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91
password_string = ""
for n in range(0, nr_letters):
    random_letter = letters[random.randint(0, len(letters) - 1)]
    password_string += random_letter
for n in range(0, nr_numbers):
    random_number = numbers[random.randint(0, len(numbers) - 1)]
    password_string += random_number
for n in range(0, nr_symbols):
    random_symbol = symbols[random.randint(0, len(symbols) - 1)]
    password_string += random_symbol
print(f"Here is your password: {password_string}")

# Hard Level - Order of characters randomized:
# e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P
password_list_2 = []
for n in range(0, nr_letters):
    random_letter = random.choice(letters)
    password_list_2.append(random_letter)
for n in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password_list_2.append(random_number)
for n in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password_list_2.append(random_symbol)
random.shuffle(password_list_2)
password_string_2 = ""
for ele in password_list_2:
    password_string_2 += ele
print(f"Here is your password: {password_string_2}")
