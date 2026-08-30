import random

emoji = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = tuple(emoji.keys())

def get_user_choice():
    while True:
        user = input("\nRock, Paper or Scissors? (r,p,s): ").lower()

        if user in choices:
            return user
        else:
            print("\nInvalid choice!")
        
def display_choices(user, comp):
    print(f"\nYou choose {emoji[user]}")
    print(f"Computer choose {emoji[comp]}")

def winner(user, comp):
    if user == comp:
        print("It's a tie!")
    elif(
        (user == 'r' and comp == 'p') or 
        (user == 'p' and comp == 's') or 
        (user == 's' and comp == 'r')):
        print("You Lose!")
    else:
        print("You Win!")

def play_game():
    while True:
        user = get_user_choice()
        comp = random.choice(choices)

        display_choices(user, comp)
        winner(user, comp)

        if input("\nDo you want to play again? (y/n): ").lower() == 'n':
            print("\nThanks for playing!!")
            break

play_game()