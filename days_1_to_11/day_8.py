# # Day 8/100 - Function Parameters & Caesar Cipher
#
# # Simple function
# def greet():
#     print("Hello")
#     print("How's it going?")
#     print("Isn't the weather nice today, eh?")
#
#
# greet()
#
#
# # Function that allows for one input
# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print(f"How do you do, {name}?")
#
#
# greet_with_name("David")
#
#
# # Function that allows for multiple inputs
# def greet_with(name, location):
#     print(f"Hello, {name}!")
#     print(f"What is it like in {location}?")
#
#
# greet_with("David", "Spain")
#
# # Function with keyword arguments
# greet_with(location="Spain", name="David")
#
#
# # Paint Area Calculator Challenge:
#
# # Write your code below this line 👇
# def paint_calc(height, width, cover):
#     number_of_cans = round((height * width) / cover)
#     number_of_cans_to_string = str(number_of_cans)
#     print(f"You'll need {number_of_cans_to_string} cans of paint.")
#
#
# # Write your code above this line 👆
# # Define a function called paint_calc() so the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))  # Height of wall (m)
# test_w = int(input("Width of wall: "))  # Width of wall (m)
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)
#
#
# # Prime Number Checker Challenge:
#
# # Write your code below this line 👇
# def is_prime_number(number):
#     is_prime = True
#     number_to_string = str(number)
#
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#
#     if is_prime:
#         print(f"{number_to_string} is prime.")
#     else:
#         print(f"{number_to_string} is not prime.")
#
#
# # Write your code above this line 👆
# n = int(input("Enter a number to see if it's prime: "))  # Check this number
# is_prime_number(number=n)

# Day 8 Project - Caesar Cipher:

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# #  e.g.
# #  plain_text = "hello"
# #  shift = 5
# #  cipher_text = "mjqqt"
# #  print output: "The encoded text is mjqqt"
#
# # HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
# # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# def encrypt(plain_text, shift_amount):
#     text_to_list = [*plain_text]
#     for n in range(0, len(text_to_list)):
#         index_of_letter = alphabet.index(text_to_list[n])
#         new_letter = index_of_letter + shift_amount
#         if new_letter > 25:
#             while new_letter > 25:
#                 new_letter -= 26
#         text_to_list[n] = alphabet[new_letter]
#     print(f"The encoded text is: {''.join(text_to_list)}")
#
#
# # TODO-3: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# # TODO-4: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by
# #  the shift amount and print the decrypted text.
# #  e.g.
# #  cipher_text = "mjqqt"
# #  shift = 5
# #  plain_text = "hello"
# #  print output: "The decoded text is hello"
#
# def decrypt(plain_text, shift_amount):
#     text_to_list = [*plain_text]
#     for n in range(0, len(text_to_list)):
#         index_of_letter = alphabet.index(text_to_list[n])
#         new_letter = index_of_letter - shift_amount
#         if new_letter < 0:
#             while new_letter < 0:
#                 new_letter += 26
#         text_to_list[n] = alphabet[new_letter]
#     print(f"The decoded text is: {''.join(text_to_list)}")
#
#
# # TODO-5: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# #  Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt
# #  *AND* decrypt a message.
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Sorry, you either misspelled the word or that isn't an option.")

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

characters = [' ', '?', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-6: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(cipher_direction, plain_text, shift_amount):
    text_to_list = [*plain_text]
    text_list_length = len(text_to_list)
    if cipher_direction == "encode":
        for n in range(0, text_list_length):
            index_of_letter = characters.index(text_to_list[n])
            new_letter = index_of_letter + shift_amount
            if new_letter > 38:
                while new_letter > 38:
                    new_letter -= 39
            text_to_list[n] = characters[new_letter]
        print(f"The encoded text is: {''.join(text_to_list)}")
    elif cipher_direction == "decode":
        for n in range(0, text_list_length):
            index_of_letter = characters.index(text_to_list[n])
            new_letter = index_of_letter - shift_amount
            if new_letter < 0:
                while new_letter < 0:
                    new_letter += 39
            text_to_list[n] = characters[new_letter]
        print(f"The decoded text is: {''.join(text_to_list)}")
    else:
        print("Sorry, you either misspelled the word or that isn't an option.")


# TODO-7: Call the caesar() function, passing over the 'direction', 'text', and 'shift' values.
# caesar(direction, text, shift)


# TODO-8: Can you figure out a way to ask the user if they want to restart the cipher program?
#  e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#  If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#  Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
restart = "yes"
while not restart == "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    restart = input("\nType 'yes' if you want to go again, otherwise type 'no'. \n").lower()
    if restart == "no":
        print("Caesar cipher shutting down...")