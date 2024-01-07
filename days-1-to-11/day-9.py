# # Day 9/100 - Dictionaries, Nesting, and the Secret Auction
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."
# };
#
# grades_dictionary = {
#     "Bob": 95,
#     "Jim": 85,
#     "Dan": 75
# };
#
# # Accessing a dictionary:
# print(programming_dictionary["Bug"]);
#
# # Adding a new key:value pair to a dictionary:
# programming_dictionary["Loop"] = "The action of running code continuously.";
#
# # Create an empty dictionary:
# empty_dictionary = {};
#
# # Delete data within a dictionary:
# programming_dictionary = {};
#
# # Edit the value of a key in a dictionary:
# grades_dictionary["Dan"] = 80;
# print(grades_dictionary);
#
# # Loop through a dictionary and print the keys:
# for grade in grades_dictionary:
#     print(grade);
#
# # Loop through a dictionary and print the values:
# for grade in grades_dictionary:
#     print(grades_dictionary[grade]);
#
# # Student Grades Challenge:
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# };
# # 🚨 Don't change the code above 👆
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {};
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     score = student_scores[student];
#     grade = "";
#     if 91 <= score <= 100:
#         grade = "Outstanding";
#     elif 81 <= score <= 90:
#         grade = "Exceeds Expectations";
#     elif 71 <= score <= 80:
#         grade = "Acceptable";
#     else:
#         grade = "Fail";
#     student_grades[student] = grade;
#
# # 🚨 Don't change the code below 👇
# print(student_grades);
#
# # Nesting a list in a dictionary:
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# };
#
# # Nesting a dictionary in a dictionary:
# city_travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# };
# print(city_travel_log["France"]["cities_visited"][0]);
# print(city_travel_log["France"]["total_visits"]);
#
# # Nesting a dictionary in a list:
# country_travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     }
# ];
# for n in range(0, len(country_travel_log)):
#     print(country_travel_log[n]["cities_visited"]);
#
# # Add dictionary to list Challenge:
# country = input("Country name: ");  # Add country name
# visits = int(input("Number of visits: "));  # Number of visits
# cities_string = input("Cities visited: ");  # Create list from string
# list_of_cities = [];
#
# if cities_string.__contains__(', '):
#     list_of_cities = list(cities_string.split(", "));
# else:
#     list_of_cities = list(cities_string.split(" "));
#
# challenge_travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ];
#
#
# # Do NOT change the code above 👆
# # TODO: Write the function that will allow new countries
# #  to be added to the travel_log.
# def add_new_country(country_name, number_of_visits, cities_visited):
#     new_country = {
#         "country": country_name,
#         "visits": number_of_visits,
#         "cities": cities_visited
#     };
#     challenge_travel_log.append(new_country)
#
#
# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities);
# print(f"I've been to {challenge_travel_log[2]['country']} {challenge_travel_log[2]['visits']} times.");
# print(f"My favourite city was {challenge_travel_log[2]['cities'][0]}.");


# Day 9 Project - Silent Auction:
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)


bids = [];


def add_new_bid(user_name, user_bid):
    new_bid = {
        "name": user_name,
        "bid": user_bid
    };
    bids.append(new_bid);


print(logo);
more_bids = True;

while more_bids:
    name = input("What is your name?: ");
    bid = int(input("What is your bid?: $"));
    add_new_bid(name, bid);
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower();
    if other_bidders == "yes":
        clear();
    else:
        more_bids = False;
        highest_bid = 0;
        highest_bidder = "";
        for n in range(0, len(bids)):
            current_bid = bids[n]["bid"];
            current_bidder = bids[n]["name"];
            if current_bid > highest_bid:
                highest_bid = current_bid;
                highest_bidder = current_bidder;
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!");
