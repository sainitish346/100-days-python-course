# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art.py
print(art.logo)

def highest_bid(bidding_dictionary):
    winner=""
    highest_bid_price=0
    #max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid_price:
            highest_bid_price=bid_amount
            winner=bidder
    print(f'the winner is {winner} bid amount is {highest_bid_price}')


continue_bidding=True
bids={}
while continue_bidding:
    name=input('what is your name?:')
    price=int(input('what is your bid amount?:$'))
    bids[name]=price
    should_continue=input('are there any other bidders type "yes" or "no"' ).lower()
    if should_continue=='no':
        highest_bid(bids)
        continue_bidding = False
    elif should_continue=='yes':
        print("\n"*20)

    else:
        print('invalid choice please enter a valid choice')


