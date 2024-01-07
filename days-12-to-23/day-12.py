# Day 12/100 - Namespaces: Local vs. Global Scope

import random;

# Day 12 Project - Number Guessing Game:

logo = """
 .---. .-. .-..----. .----. .----.    .---. .-. .-..----.   .-. .-..-. .-..-.   .-..----. .----..----. 
/   __}| { } || {_  { {__  { {__     {_   _}| {_} || {_     |  `| || { } ||  `.'  || {}  }| {_  | {}  }
\  {_ }| {_} || {__ .-._} }.-._} }     | |  | { } || {__    | |\  || {_} || |\ /| || {}  }| {__ | .-. }
 `---' `-----'`----'`----' `----'      `-'  `-' `-'`----'   `-' `-'`-----'`-' ` `-'`----' `----'`-' `-'
""";

print(logo);
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.");

difficulty = "";
attempts = 0;

while not difficulty == "easy" or not difficulty == "hard":
    difficulty = input(
        "Choose a difficulty. Type 'easy' for 10 attempts to guess the number or 'hard' for 5 attempts: ").lower().strip();

    if difficulty == "easy":
        attempts = 10;
        break;
    elif difficulty == "hard":
        attempts = 5;
        break;
    else:
        print("Invalid input - type 'easy' or 'hard'.");

random_number = random.randint(0, 100);

while attempts > 0:
    if attempts == 1:
        print("This is your last attempt...");
        guess = int(input("Make a guess: "));
        if guess > random_number:
            print("That's too high, you lose...");
        elif guess < random_number:
            print("That's too low, you lose...");
        elif guess == random_number:
            print("You guessed it correctly, you win!");
        break;
    else:
        print(f"You have {attempts} attempts remaining to guess the number.");
        guess = int(input("Make a guess: "));
        if guess > random_number:
            print("Too high.\nGuess again.");
            attempts -= 1;
        elif guess < random_number:
            print("Too low.\nGuess again.");
            attempts -= 1;
        elif guess == random_number:
            print("You guessed it correctly, you win!");
            break;
