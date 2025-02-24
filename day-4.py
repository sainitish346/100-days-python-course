import random
user_choice=int(input('what do you choose?Type 0 for Rock, 1 for Paper, 2 for Scissors'))
computer_choice=random.randint(0,2)
if computer_choice==2 and user_choice==0:
    print('you win')
elif computer_choice==0 and user_choice==2:
    print('you lose')
elif computer_choice>user_choice:
    print('you lose')
elif computer_choice == user_choice
else:
    print('you type a invalid number you lose!')
