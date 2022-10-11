import random
import os
from game_data import data
from art import logo
from art import vs
# option_one = data[randint(0,(len(data)-1))]
# option_two = data[randint(0,(len(data)-1))]
# score_one = option_one["follower_count"]
# score_two = option_two["follower_count"]
# # print(option_one["follower_count"])
# # print(option_two["follower_count"])

# def format():
#     print(logo)
#     print(f"Compare A: {option_one['name']}, a {option_one['description']}, from {option_one['country']}.")
#     print (vs)
#     print(f"Compare A: {option_two['name']}, a {option_two['description']}, from {option_two['country']}.")
#     user_choice = input(("Who has more followers? Type 'A' or 'B': "))

# format()

# if format() == "A":
#     print("Hey")

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right.Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("cls")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()