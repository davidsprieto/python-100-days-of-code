# Day 3/100: Control Flow and Logical Operators

print("Welcome to the roller coaster.")
height = int(input("What is your height in centimeters? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Would like to have a photo taken? It will be an extra $3 - Yes or No? ")
    if wants_photo == "Yes":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you don't meet the height requirement to ride this roller coaster...")


# BMI 2.0 Challenge:
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

bmi = round(weight / (height ** 2))

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


# Leap Year Challenge:
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

if year % 4 != 0:
    print("Not a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")


# Pizza Order Challenge
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your final bill is: ${bill}.")


# Love Calculator Challenge:
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names_combined_to_lowercase = (name1 + name2).lower()

names_combined_true_count = names_combined_to_lowercase.count("t") + names_combined_to_lowercase.count("r") + names_combined_to_lowercase.count("u") + names_combined_to_lowercase.count("e")
names_combined_love_count = names_combined_to_lowercase.count("l") + names_combined_to_lowercase.count("o") + names_combined_to_lowercase.count("v") + names_combined_to_lowercase.count("e")

love_score_to_string = str(names_combined_true_count) + str(names_combined_love_count)
love_score_to_int = int(love_score_to_string)

if (love_score_to_int < 10) or (love_score_to_int > 90):
    print(f"Your score is {love_score_to_int}, you go together like coke and mentos.")
elif 40 <= love_score_to_int <= 50:
    print(f"Your score is {love_score_to_int}, you are alright together.")
else:
    print(f"Your score is {love_score_to_int}.")


# Day 3 Project - Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
left_or_right = input("You're at a fork in the road, which direction do you want to go? On the left there is a trail leading to a cave, on the right there is a trail leading to the top of a mountain. Type 'Left' or 'Right' \n").lower()
if left_or_right == "left":
    swim_or_wait = input("You've come to the cave where there is a body of water inside that leads to a waterfall. While standing there you see a man standing by the waterfall waving at you to come across. Do you swim across or wait? Type 'Swim' or 'Wait' \n").lower()
    if swim_or_wait == "wait":
        red_blue_or_yellow = input("Since you decided to wait patiently, a small raft and oar drift to you. You hop in and paddle across to the waterfall. Once there, behind it you see there are 3 doors. One red, one blue, and one yellow. Which door do you wish to open? Type 'Red', 'Blue', or 'Yellow' \n").lower()
        if red_blue_or_yellow == "red":
            print("You open the red door and a pirate slashes you with his sword. Game Over.")
        elif red_blue_or_yellow == "blue":
            print("You open the blue door and see a treasure chest! As you walk closer to it a false floor opens up and you fall 30 feet into a pile of sharp spears. Game Over.")
        elif red_blue_or_yellow == "yellow":
            print("You open the yellow door and it's a room full of ancient treasure, looking to your right you see a large pirate ship that can fit all the treasure. You load the treasure onto the ship and sail away into the sunset. You Win!")
    else:
        print("While swimming to the man an alligator attacks you. Game Over.")
else:
    print("While hiking the trail a large boulder rolls off the side of a cliff and crushes you. Game Over.")
