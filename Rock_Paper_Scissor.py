import random

choices = ('r', 'p', 's')
emoji = {'r': '🪨', 'p': '📃', 's': '✂️'}

while True:
    user = input("\nRock, Paper or Scissors? (r,p,s): ").lower()

    if user not in choices:
        print("\nInvalid choice!")
        continue

    comp = random.choice(choices)
    print(f"\nYou choose {emoji[user]}")
    print(f"Computer choose {emoji[comp]}")

    if user == comp:
        print("It's a tie!")
    elif(
        (user == 'r' and comp == 'p') or 
        (user == 'p' and comp == 's') or 
        (user == 's' and comp == 'r')):
        print("You Lose!")
    else:
        print("You Win!")

    if input("\nDo you want to play again? (y/n): ").lower() == 'n':
        print("\nThanks for playing!!")
        break