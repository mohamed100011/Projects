import random
from art import logo, vs
from data_name import data


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description} form {account_country}"


def account_follower(ask_user, a_follower, b_follower):
    if a_follower > b_follower:
        return ask_user == "a"
    else:
        return ask_user == "b"


print(logo)
score = 0

game_should_continue = True

while game_should_continue:

    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    ask_user = input("Guess A Or B More Follower's: ").lower()

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = account_follower(ask_user, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f"You're right And Cuntry Score Is {score}")
    else:
        print(f"Sorry You're worng And Final Score Is {score}")
        game_should_continue = False
