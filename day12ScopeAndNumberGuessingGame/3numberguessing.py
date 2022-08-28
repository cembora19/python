from random import randint

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def chech_answer(guess, answer, turns):
    """check answer against guess. returns the number of turns remaining"""
    if guess>answer:
        print("too high")
        return turns-1
    elif guess<answer:
        print("too low")
        return turns-1
    else:
        print(f"you got it! the answer was {answer}")

def set_difficulty():
    level=input("choose a difficulty. type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("welcome to the number guessing game!")
    print("i'm thinking of a number between 1 and 100")
    answer=randint(1,100)
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts remaining to guess to number.")
        guess=int(input("make a guess:"))
        turns=chech_answer(guess,answer,turns)
        if turns==0:
            print("you've run out of guesses, you lose.")
            return
        elif guess!=answer:
            print("guess again")