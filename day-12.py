logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
import random
import art
print(art.logo)

def choose_number():
    a=random.randint(1,10)
    return a

def easy_game(num):
    attempts=10
    value=int(input('enter your number'))
    while attempts!=0:
        if value > num:
            attempts-=1
            print(f'{value} is too high, you have {attempts} attempts')
            value = int(input('enter your number'))
        else:
            attempts-=1
            print(f'{value} is too low, you have {attempts} attempts')
            value = int(input('enter your number'))
    if value==num:
        print('you win')
    else:
        print('you loose')
        print(f'the number is {num}')

def hard_game(num):
    attempts=5
    print(f'you have {attempts} attempts')
    value=int(input('enter your number'))
    while attempts!=0 and value!=num:
        if value>num:
            attempts-=1
            print(f'{value} is too high, you have {attempts} attempts')
        elif value<num:
            attempts-=1
            print(f'{value} is too low, you have {attempts} attempts')
        if value!=num and attempts!=0:
            value=int(input('enter your number'))
    if value==num:
        print('you win')
    else:
        print('you loose')
        print(f'the number is {num}')

print('welcome to the number guessing game')
print("I'am guessing a number between 1 to 100")
number=choose_number()
choice=input('choose diffcuilty: easy or hard').lower()
if choice=="easy":
    easy_game(number)
else:
    hard_game(number)
