import random
user_win = False
computer_win = False

def input_template():
    print("-------------------")
    print("|     |     |     |")
    print("|  1  |  2  |  3  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print("|  4  |  5  |  6  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print("|  7  |  8  |  9  |")
    print("|     |     |     |")
    print("-------------------")
    print("given format for input\n")

def display():
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {dic[1]}  |  {dic[2]}  |  {dic[3]}  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {dic[4]}  |  {dic[5]}  |  {dic[6]}  |")
    print("|     |     |     |")
    print("-------------------")
    print("|     |     |     |")
    print(f"|  {dic[7]}  |  {dic[8]}  |  {dic[9]}  |")
    print("|     |     |     |")
    print("-------------------")

def user_choice():
    while True:
        user_choice = int(input("Enter your choice(1-9): "))
        if user_choice > 9 or user_choice < 1:
            print("!Choice must be in between 1-9")
        elif not dic[user_choice] == ' ':
            print("!The choice has been used")
        else:
            dic[user_choice] = 'X'
            break

def computer_choice():
    computer_choice = random.choice([i for i in dic if dic[i] == ' '])
    dic[computer_choice] = 'O'
    display()

def is_win():
    win_combinations = [
            (1,2,3), (4,5,6), (7,8,9),
            (1,4,7), (2,5,8), (3,6,9),
            (1,5,9), (3,5,7)
        ]
    
    for a,b,c in win_combinations:
        if dic[a] == dic[b] == dic[c] == 'X':
            return "User Win!!!"
        elif dic[a] == dic[b] == dic[c] == 'O':
            return "Computer Win!!!"

    if " " not in dic.values():
            return "It's a Draw!!!"        

    return False
        
dic = {1: " ",
       2: " ",
       3: " ",
       4: " ",
       5: " ",
       6: " ",
       7: " ",
       8: " ",
       9: " "}

input_template()

while True:
    if is_win():
        print(is_win())
        break
    else:
        user_choice()
    
    if is_win():
        display()
        print(is_win())
        break
    else:
        computer_choice()
    
