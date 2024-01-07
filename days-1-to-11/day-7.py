# Day 7/100: Hangman Project

import random

# # Step 1:
#
# word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen_word = random.choice(word_list)
# chosen_word_length = len(chosen_word)
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter: ").lower()
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# if guess in chosen_word:
#     print("True")
# else:
#     print("False")
#
# # Step 2:
#
# # Testing code
# print(f'The chosen word is: {chosen_word}.')
#
# # TODO-4: - Create an empty List called display.
# # For each letter in the chosen_word, add a "_" to 'display'.
# # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = []
# for n in range(0, chosen_word_length):
#     display.append("_")
#
# # TODO-5: - Loop through each position in the chosen_word;
# # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for n in range(0, chosen_word_length):
#     if chosen_word[n] == guess:
#         display[n] = guess
#
# # TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)
#
# # Step 3:
#
# # TODO-7: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters
# #  in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# chosen_word_length = len(chosen_word)
#
# display = []
# for n in range(0, chosen_word_length):
#     display.append("_")
#
# while "_" in display:
#     guess = input("Guess a letter: ").lower()
#     if guess in chosen_word:
#         for n in range(0, chosen_word_length):
#             if chosen_word[n] == guess:
#                 display[n] = guess
#     print(display)
#
# # Step 4:
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# # TODO-8: - Create a variable called 'lives' to keep track of the number of lives left.
# #  Set 'lives' to equal 6.
# lives = 6
#
# # TODO-9: - If guess is not a letter in the chosen_word,
# #  Then reduce 'lives' by 1.
# #  If lives goes down to -1 then the game should stop and it should print "You lose."
# #  Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
# while lives > -1:
#     guess = input("Guess a letter: ").lower()
#     if guess in chosen_word:
#         for n in range(0, chosen_word_length):
#             if chosen_word[n] == guess:
#                 display[n] = guess
#     else:
#         print(stages[lives])
#         lives -= 1
#         if lives == -1:
#             print("You lose.")
#
#     # TODO-10: - Join all elements in the list and turn it into a string
#     print(f"{' '.join(display)}")

# Step 5:

# TODO-11 - Put it all together - Complete the Hangman Game Project
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]
chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

display = []
for n in range(0, chosen_word_length):
    display.append("_")

letters_guessed = []

lives = 6

print(logo)

while lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in letters_guessed:
        print(f"You've already guessed '{guess}'. Letters guessed: {', '.join(letters_guessed)}")
    elif guess in chosen_word:
        for n in range(0, chosen_word_length):
            if chosen_word[n] == guess:
                display[n] = guess
                print(f"Nice, '{guess}' is in the word.")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if guess not in letters_guessed:
        letters_guessed.append(guess)
    print(f"{' '.join(display)}")
    print(stages[lives])
    if lives == 0:
        print("You lose.")