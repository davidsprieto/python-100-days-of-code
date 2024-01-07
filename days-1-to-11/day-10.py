# # Day 10/100 - Functions with Outputs
#
# def format_name(f_name, l_name):
#     """Takes a string first name and string last name as inputs then returns the string title case version of the name."""
#     if f_name.strip() == "" or l_name.strip() == "":
#         return "Invalid input(s)";
#     formatted_f_name = f_name.title();
#     formatted_l_name = l_name.title();
#     return f"{formatted_f_name} {formatted_l_name}";
#
#
# first_name = input("What is your first name?: ");
# last_name = input("what is your last name?: ");
# formatted_name = format_name(first_name, last_name);
#
# print(formatted_name);
#
#
# # Days in Month Challenge
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True;
#             else:
#                 return False;
#         else:
#             return True;
#     else:
#         return False;
#
#
# # TODO: Add more code here 👇
# def days_in_month(year, month):
#     if month < 1 or month > 12:
#         return "Month must be a number from 1 to 12.";
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
#     is_leap_year = is_leap(year);
#     index = month - 1;
#     if is_leap_year and month == 2:
#         return month_days[index] + 1;
#     else:
#         return month_days[index];
#
#
# # 🚨 Do NOT change any of the code below
# input_year = int(input("Enter a year: "));  # Enter a year
# input_month = int(input("Enter a month by it's number (January = 1, February = 2, etc..): "));  # Enter a month
# days = days_in_month(input_year, input_month);
# if input_month < 1 or input_month > 12:
#     print(f"{days}");
# else:
#     print(f"The number of days in that month for {input_year} is {days} days.");


# Day 10 Project - Calculator
logo = """
 _____________________
|  _________________  |
| | Python       0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2;


def subtract(n1, n2):
    return n1 - n2;


def multiply(n1, n2):
    return n1 * n2;


def divide(n1, n2):
    return n1 / n2;


operations_functions_dictionary = {"+": add, "-": subtract, "*": multiply, "/": divide};


# Recursive function
def calculator():
    print(logo);
    should_continue = True;
    num1 = float(input("Enter your first number: ").strip());

    while should_continue:

        for operation in operations_functions_dictionary:
            print(operation);

        operation = input("Choose an operation using the symbols (+, -, *, or /): ").strip();
        num2 = float(input("Enter your second number: ").strip());

        calculation = operations_functions_dictionary[operation];
        result = calculation(num1, num2);
        print(f"{num1} {operation} {num2} = {result}.");

        user_continue = input(
            f"Type 'c' to continue calculating with {result}, type 'n' to start a new calculation, type 'e' to exit: ").lower().strip();

        if user_continue == "c":
            num1 = result;
        elif user_continue == "e":
            print("✌️");
            return;
        else:
            should_continue = False;
            calculator();


calculator();
