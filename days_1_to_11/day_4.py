# Day 4/100: Randomization and Python Lists

import random

# Using random module

# Random Integer - random.randint()
random_int = random.randint(1, 10)
print(random_int)

# Random Float - random.random()
random_float = random.random()
print(random_float)

# Heads or Tails Challenge
random_num = random.randint(0, 1)
if random_num == 0:
    print("Tails")
else:
    print("Heads")

# Lists
states_of_america = ["Delaware", "Pennsylvania", "Texas", "Wisconsin"]
print(states_of_america)

# Banker Roulette Challenge

# .split() method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_length = len(names)
random_index = random.randint(0, names_length - 1)
random_name = names[random_index]
print(f"{random_name} is going to buy the meal today!")

# Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])


# Treasure Map Challenge

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
t_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column = int(position[0]) - 1
row = int(position[1]) - 1
t_map[row][column] = "X"
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Day 4 Project - Rock, Paper, Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_rock_paper_or_scissors = ["rock", "paper", "scissors"]
user_rock_paper_or_scissors = input("What do you choose - Rock, Paper, or Scissors? ").lower()
computer_rock_paper_scissors = list_rock_paper_or_scissors[random.randint(0, 2)]

if user_rock_paper_or_scissors == "rock":
    print(f"\nYou chose: \n{rock}")
elif user_rock_paper_or_scissors == "paper":
    print(f"\nYou chose: \n{paper}")
elif user_rock_paper_or_scissors == "scissors":
    print(f"\nYou chose: \n{scissors}")

if computer_rock_paper_scissors == "rock":
    print(f"Computer chose: \n{rock}")
elif computer_rock_paper_scissors == "paper":
    print(f"Computer chose: \n{paper}")
elif computer_rock_paper_scissors == "scissors":
    print(f"Computer chose: \n{scissors}")

if (user_rock_paper_or_scissors == "rock") and (computer_rock_paper_scissors == "rock"):
    print("Draw")
elif (user_rock_paper_or_scissors == "rock") and (computer_rock_paper_scissors == "paper"):
    print("You lose...")
elif (user_rock_paper_or_scissors == "rock") and (computer_rock_paper_scissors == "scissors"):
    print("You win!")
elif (user_rock_paper_or_scissors == "paper") and (computer_rock_paper_scissors == "paper"):
    print("Draw")
elif (user_rock_paper_or_scissors == "paper") and (computer_rock_paper_scissors == "scissors"):
    print("You lose...")
elif (user_rock_paper_or_scissors == "paper") and (computer_rock_paper_scissors == "rock"):
    print("You win!")
elif (user_rock_paper_or_scissors == "scissors") and (computer_rock_paper_scissors == "scissors"):
    print("Draw")
elif (user_rock_paper_or_scissors == "scissors") and (computer_rock_paper_scissors == "rock"):
    print("You lose...")
elif (user_rock_paper_or_scissors == "scissors") and (computer_rock_paper_scissors == "paper"):
    print("You win!")
