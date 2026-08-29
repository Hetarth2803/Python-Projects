import random

while True:
    user_input = input("Roll the Dice? (y/n): ").lower()
    
    if user_input == 'y':
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print(f"({dice_1}, {dice_2})\n")
        #print(f"({random.randint(1,6)}, {random.randint(1,6)})")    

    elif user_input == 'n':
        print("\nThanks for playing!")
        break

    else:
        print("\nInvalid choice!\n")