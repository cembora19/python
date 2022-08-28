import random
numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print("Welcome to the number guessing game!\n I'm thinking of a number between 1 and 100")
play_again=True
# while not play_again:
def game():
    random_number=random.choice(numbers)
    difficult=input("Choose a difficult. Type 'easy' or 'hard'. ")
    if difficult=="easy":
        step=10
    elif difficult=="hard":
        step=5
    is_game_over=True
    print(f"random number is: {random_number}")
    while is_game_over and step!=0:
        print(f"You have {step} attempts remaining to guess number.")
        hold_number=int(input("Make a guess: "))
        if hold_number>random_number:
            print("Too high.\n Guess Again.")
            step-=1
        elif hold_number<random_number:
            print("Too low. \n Guess Again.")
            step-=1
        elif hold_number==random_number:
            print(f"You got it. The answer is {random_number}.")
            is_game_over=False
    if input("if you want to play again please type 'yes'")=="yes":
        game()
game()