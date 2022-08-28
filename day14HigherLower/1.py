from data import data
from art import logo, vs
import random
from replit import clear
print(logo)
def format_data(account):
    account_name=account["name"]
    account_decr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_decr}, from {account_country}"
def game():
    counter=0
    game_end=0
    while game_end==0:
        account_a=random.choice(data)
        account_b=random.choice(data)
        if account_a==account_b:
            account_b=random.choice(data)
        print(f"Compare a: {format_data(account_a)}")
        print(vs)
        print(f"compare b: {format_data(account_b)}")
        choose_option=input("who has more followers? Type 'a' or 'b': ")
        if account_a["follower_count"]>account_b["follower_count"] and choose_option=="a":
            counter+=1
            account_b=random.choice(data)
            if account_b==account_a:
                account_b=random.choice(data)
            clear()
            print(f"You're right! current score: {counter}")
        elif account_b["follower_count"]>account_a["follower_count"] and choose_option=="b":
            counter+=1
            account_a=account_b
            account_b=random.choice(data)
            if account_b==account_a:
                account_b=random.choice(data)
            clear()
            print(f"You're right! current score: {counter}")
        else:
            print(f"Sorry, that's wrong. Final Score: {counter}")
            game_end=1
            play_again=input("If you want to play again type 'yes': ")
            if play_again=="yes":
                clear()
                print(logo)
                game()
game()