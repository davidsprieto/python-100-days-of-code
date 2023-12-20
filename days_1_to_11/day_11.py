# Day 11/100 - Blackjack Capstone Project

import random;

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""";

print(logo);

user_play_again = True;

user_play_blackjack = input("Do you want to play blackjack? Type 'y' for yes or 'n' for no: ").lower().strip();

if user_play_blackjack == "y":
    user_play_blackjack = True;
else:
    print("Maybe some other time then ✌️");
    user_play_blackjack = False;

while user_play_blackjack and user_play_again:
    cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10];
    user_hand = [];
    computer_hand = [];


    def deal_a_card():
        random_index = random.randint(0, len(cards) - 1);
        card = cards[random_index];
        del cards[random_index];
        return card;

    # Shuffle array:
    random.shuffle(cards);
    # Deal a card to user:
    user_card_1 = deal_a_card();
    user_hand.append(user_card_1);
    # Deal a card to computer:
    computer_card_1 = deal_a_card();
    computer_hand.append(computer_card_1);
    # Deal a second card to user:
    user_card_2 = deal_a_card();
    user_hand.append(user_card_2);

    user_hand_total = sum(user_hand);
    computer_hand_total = sum(computer_hand);


    def print_user_hand():
        print(f"Your cards: {user_hand}, your total: {user_hand_total}");


    def print_computer_hand(computer_hand_total):
        print(f"Computer's hand: {computer_hand}, computer's total: {computer_hand_total}");


    def check_computer_hand_total(computer_hand_total):
        print("The computer will first reveal its face down card and if the total is less than 16 the computer will continue to hit until its total is 17 or greater.");
        while computer_hand_total <= 16:
            computer_card_hit = deal_a_card();
            if computer_card_hit == 11 and computer_hand_total + computer_card_hit > 21:
                computer_card_hit = 1;
            computer_hand.append(computer_card_hit);
            computer_hand_total += computer_card_hit;
            print_computer_hand(computer_hand_total);
        if computer_hand_total > 21:
            print("Computer busts, you win!");
        elif computer_hand_total == 21 and user_hand_total == 21:
            print("You and the computer both have 21, it's a push!");
        elif computer_hand_total == 21 and not user_hand_total == 21:
            print("Computer has 21, you lose...");
        elif computer_hand_total < user_hand_total:
            print("You have a higher total of cards, you win!");
        elif computer_hand_total > user_hand_total:
            print("Computer has a greater total, you lose...");
        elif computer_hand_total == user_hand_total:
            print("You and the computer have the same totals, it's a push!");

    user_hit = True;

    if user_hand_total == 21:
        print_user_hand();
        print("Blackjack! Let's see the computer's face down card...");
        computer_card_2 = deal_a_card();
        computer_hand.append(computer_card_2);
        computer_hand_total += computer_card_2;
        print_computer_hand(computer_hand_total);
        if computer_hand_total == 21:
            print("You both got BlackJack, it's a push!");
        else:
            print("Computer doesn't have Blackjack, you win!");
        user_hit = False;
    else:
        print_user_hand();
        print_computer_hand(computer_hand_total);

    while user_hit:
        user_hits = input("Hit or Stay? Type 'h' for hit or 's' for stay: ").lower().strip();
        if user_hits == "h":
            user_card_hit = deal_a_card();
            if user_card_hit == 11 and user_hand_total + user_card_hit > 21:
                user_card_hit = 1;
            user_hand.append(user_card_hit);
            user_hand_total += user_card_hit;
            print_user_hand();
            if user_hand_total == 21:
                user_hit = False;
                check_computer_hand_total(computer_hand_total);
            elif user_hand_total < 21:
                user_hit = True;
            elif user_hand_total > 21:
                user_hit = False;
                print("Bust, you lose...");
            else:
                user_hit = True;
        else:
            user_hit = False;
            check_computer_hand_total(computer_hand_total);

    user_play_again = input("Do you want to play another hand? Type 'y' for yes or 'n' for no: ").lower().strip();

    if user_play_again == "y":
        user_play_again = True;
    else:
        print("Thanks for playing 🤙");
        user_play_again = False;

# PROGRAM END #