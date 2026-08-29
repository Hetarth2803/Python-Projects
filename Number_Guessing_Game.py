import random

win = random.randint(1, 100)
count = 0

while True:
    
    try:
        guess = int(input("\nGuess a number between 1 to 100: "))
        count += 1
        
        if guess > win:
            print("\nToo High!")
        elif guess < win:
            print("\nToo Low!")
        else:
            print(f"\nCongratulations!, You Guessed the number in {count} guesses.")
            break
    
    except ValueError:
        print("\n!!!Please enter a valid number")