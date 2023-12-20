# Day 13/100 - Debugging

import random;


# # Describe the Problem
# # range() method second parameter is not inclusive, therefore, the loop never reaches 20 - it only reaches 19.
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it 🤘");
#
#
# my_function();


# # Reproduce the Bug
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"];
# # dice_num = random.randint(1, 6); ---> List index out of range error
# dice_num = random.randint(0, 5);
# print(dice_images[dice_num]);


# # Play Computer
# year = int(input("What's your birth year?: "));
# if 1965 <= year <= 1980:
#     print("You are a Gen X.");
# elif 1980 < year <= 1996:
#     print("You are a millennial.");
# elif 1996 < year <= 2012:
#     print("You are a Gen Z.");


# # Fix the Errors
# age = int(input("How old are you?: "));
# if age > 18:
#     print(f"You can drive at age {age}.");


# # Print is Your Friend
# pages = int(input("Number of pages: "));
# print(F"pages = {pages}");
# words_per_page = int(input("Number of words per page: "));
# print(f"words per page = {words_per_page}");
# total_words = pages * words_per_page;
# print(f"total words = {total_words}");


# Use a Debugger
def mutate(a_list):
    b_list = [];
    for item in a_list:
        new_item = item * 2;
        b_list.append(new_item);
    print(b_list);


mutate([1, 2, 3, 5, 8, 13]);
