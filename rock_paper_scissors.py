import random

choices = ['rock', 'paper', 'scissors']
comp_choice = random.choice(choices)
print('Computer choice: ', comp_choice)

user_choice = input('Do you want rock, papare, or scissors?\n')
if user_choice not in choices:
    print('Cheater!!!')
else:
    if comp_choice == user_choice:
        print('TIE')
    elif comp_choice == 'scissors' and user_choice == 'rock':
        print('WIN')
    elif comp_choice == 'rock' and user_choice == 'paper':
        print('WIN')
    elif comp_choice == 'paper' and user_choice == 'scissors':
        print('WIN')
    else:
        print('You loose')
