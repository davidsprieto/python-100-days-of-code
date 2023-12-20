# Day 2/100: Data Types

# String
print("Hello")
print("Hello"[4])
print("123" + "45")

# Integer
print(123)
print(123 + 45)

# Float
print(3.14159)

# Boolean
print(True)
print(False)

# type() method
print(type("Hello"))
print(type(123))
print(type(3.14159))
print(type(True))

# type conversion - str(), int(), float()
num_of_chars = len(input("What is your name? "))
num_of_chars_to_string = str(num_of_chars)
print("Your name has " + num_of_chars_to_string + " characters in it.")

# Mathematical Operations
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(5 % 4)
print(2 ** 2)  # 2 to the power of 2
print(4 // 3)  # floor division, rounds down

# F Strings
score = 0
height = 1.8
isWinning = True
print(f"This is how F Strings in python work: Your score is {score}. Your height is: {height}. Are you winning?: {isWinning}\n")

# Day 2 Project - Tip Calculator
print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill_with_tip = (bill_amount * (tip_amount / 100)) + bill_amount
num_people_to_split_total_bill = int(input("How many people to split the bill? "))
total_amount_to_pay = round(total_bill_with_tip / num_people_to_split_total_bill, 2)
total_amount_to_pay = "{:.2f}".format(total_amount_to_pay)
print(f"Each person should pay: ${total_amount_to_pay}")
