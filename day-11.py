logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score,c_score):
    if u_score==c_score:
        print('its draw')
    elif c_score==0:
        print('you loose,opponent has blackjack')
    elif u_score==0:
        print('you win you got blackjack')
    elif u_score>21:
        print('you went over, computer wins')
    elif c_score>21:
        print('computer went over, you win')
    elif u_score>c_score:
        print('you win')
    else:
        print('computer wins')
def play_game():
    print(art.logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f'user cards {user_cards} ,score= {user_score}')
        print(f'computer first card {computer_cards[0]}')

        if user_score==0 or computer_score==0 or user_score > 21:
            #print('you loose')
           is_game_over=True
        else:
                choice=input('do you want continue yes or no').lower()
                if choice=='yes':
                   user_cards.append(deal_card())
                else:
                    is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f'your hand is:{user_cards},your score is {user_score}')
    print(f'computer hand is:{computer_cards},computer score{computer_score}')
    print(compare(user_score,computer_score))

while input('want to paly game type yes or no ').lower()=='yes':
    print('\n'*20)
    play_game()